import urlparse
import xlwt
import datetime
import xhtml2pdf.pisa as pisa
import string
import json
import reportlab
import StringIO
import ast
import os
from django.contrib import auth
from django.utils.timezone import localtime, now
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext, Context
from appWeb.models import *
from appWeb.forms import *
from pFuhrmann.settings import *
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.http import *
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from datetime import *
from django.core import serializers
from django.conf import settings
from django.template.loader import get_template
from datetime import datetime
from django.template.context import RequestContext
from django.core.context_processors import csrf
from random import choice
from wkhtmltopdf import *
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404 
from django.core.mail import EmailMessage
import cairo
import pycha.bar
import pycha.pie
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pycha.line

# ********************************* Estadisticas *********************************
def line(request):
    cantC = [] #obtengo las commpras de cada representante
    rNro = [] #obtengo los id de representantes
    compras = [] #obtengo cantidad de compras
    for r in Representante.objects.all():
        rNro.append([r.NroLegajo])
        cantC.append(CompraLote.objects.all().filter(Representante = r))
    for c in cantC:
        compras.append([c.count()]) 
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)

    dataSet = (
        
        ('C', [(j, m[0]) for j, m in enumerate(compras)]),
        )

    options = {
        'axis': {
            'x': {
                # en label tengo los nros de representantes sobre x
                # en val tengo la cantidad de compras de cada represebtabte
                'ticks': [dict(v=j, label=rNro[0+j]) for j, m in enumerate(compras)],
                'label': 'NroLegajo Representantes',
              
            },  
            'y': {                
                'ticksCount': [dict(v=j, label=m[0]) for j, m in enumerate(compras)],
                'label': 'Cantidad Compras',
              
            },    
         
        },
        'background': {
            'chartColor': '#ffeeff',
            'baseColor': '#ffffff',
            'lineColor': '#444444'
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'green',
            },
        },
        'legend': {
            'hide': True,
        },
    }
    chart = pycha.line.LineChart(surface, options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('static/img/line.png')
    return render_to_response('Estadisticas/estadisticasRepresentantes2.html', context_instance=RequestContext(request))

def estadisticasRepresentantes(request):
    cantC = [] #obtengo las commpras de cada representante
    rNro = [] #obtengo los id de representantes
    compras = [] #obtengo cantidad de compras

    for r in Representante.objects.all():
        rNro.append([r.NroLegajo])
        cantC.append(CompraLote.objects.all().filter(Representante = r))
    for c in cantC:
        compras.append([c.count()]) 
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,650, 650)
    dataSet = (
        
        ('C', [(j, m[0]) for j, m in enumerate(compras)]),
        )
    options = {
        'legend': {'hide': True},
        'axis': {
            'x': {
                # en label tengo los nros de representantes sobre x
                # en val tengo la cantidad de compras de cada represebtabte
                'ticks': [dict(v=j, label=rNro[0+j]) for j, m in enumerate(compras)],
                'label': 'NroLegajo Representantes',
                'rotate': 25
            },  
            'y': {                
                'ticksCount': [dict(v=j, label=m[0]) for j, m in enumerate(compras)],
                'label': 'Cantidad Compras',
                'rotate': 25
            },    
        },
        'background': {
            'chartColor': '#ffeeff',
            'baseColor': '#ffffff',
            'lineColor': '#444444'
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'blue',
            },
        },
        'padding': {
            'left': 1,
            'bottom': 1,
            'top': 2,
            'right': 1,
        },
        'title': 'Compras - Representantes'
    }
    chart = pycha.bar.VerticalBarChart(surface, options)
    chart.addDataset(dataSet)   
    chart.render()
    surface.write_to_png('static/img/estadisticasRe.png')
    return render_to_response('Estadisticas/estadisticasRepresentantes.html', context_instance=RequestContext(request))

def estadisticasMaq(request):
    return render_to_response('Estadisticas/estadisticasMaquinarias.html', context_instance=RequestContext(request))


def estadisticasMaquinarias(request, FI, FF):
    listaHs = []
    nMaq= []
    listaProd = []

    FI = FI + " 00:00:00 GMT"
    FF = FF + " 00:00:00 GMT"
    FIs = datetime.strptime(FI, '%d %m %Y %H:%M:%S %Z') # Fecha Desde lo convierto en datetime
    FFs = datetime.strptime(FF, '%d %m %Y %H:%M:%S %Z') # Fecha hasta lo convierto en datetime
    
    for m in Maquinaria.objects.all():
        nMaq.append([m.NroSerie])
        listaProd.append(Produccion.objects.all().filter(Maquinaria = m)) # Todas las Maquinas

    for prod in listaProd:
        segundos = 0
        if not prod:  # Si la maquina nunca fue usada tiene 0 horas
            listaHs.append([0])
        else: # Si no recorro las producciones
            for p in prod:
                if p.FechaInicio != None: # Me fijo que la produccion haya iniciado
                    #Debo ver cuales producciones deben registrarse
                    pFI = p.FechaInicio  # datetime
                    if p.FechaFin == None:
                        pFF = datetime.now()
                    else:
                        pFF = p.FechaFin # datetime
                    
                    # Controlo que las producciones tengan dias dentro de las fechas ingresadas
                    if FFs < pFI:   # 0 horas 1 a 3 
                        break
                    elif FIs > pFF: # 0 horas
                        break
                    # Calculo tiempo
                    elif FIs > pFI and FFs > pFF:  # Si la fecha desde ingresada es mayor y fecha fin es mayor             
                        time = (pFF - FIs)
                        segundos = segundos + time.total_seconds() 
                    elif FIs > pFI and FFs < pFF:  # Si la fecha desde ingresada es mayor y fecha fin es menor               
                        time = (FFs - FIs)
                        segundos = segundos + time.total_seconds() 
                    elif FIs < pFI and FFs > pFF:  # Si la fecha desde ingresada es menor y fecha fin es mayor           
                        time = (pFF - pFI)
                        segundos = segundos + time.total_seconds() 
                    elif FIs < pFI and FFs < pFF:  # Si la fecha desde ingresada es menor y fecha fin es menor              
                        time = (FFs - pFI)
                        segundos = segundos + time.total_seconds() 
            listaHs.append([segundos])
    
    # print nMaq
    # print listaHs

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,650, 650)

    dataSet = (
        
        ('C', [(j, m[0]) for j, m in enumerate(listaHs)]),
        )

    options = {
        'legend': {'hide': True},
        'axis': {
            'x': {
                # en label tengo los nros de representantes sobre x
                # en val tengo la cantidad de compras de cada represebtabte
                'ticks': [dict(v=j, label=nMaq[0+j]) for j, m in enumerate(listaHs)],
                'label': 'Nro Serie Maquinaria',
                'rotate': 25
            },  
            'y': {                
                'ticksCount': [dict(v=j, label=m[0]) for j, m in enumerate(listaHs)],
                'label': 'Tiempo',
                'rotate': 25
            },    
        },
        'background': {
            'color': '#eeeeff',
            'lineColor': '#444444'
 
            
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'blue',
            },
        },
        'padding': {
            'left': 1,
            'bottom': 1,
            'top': 2,
            'right': 1,
        },
        'title': 'Tiempo en produccion'
    }
    chart = pycha.bar.VerticalBarChart(surface, options)
    chart.addDataset(dataSet)   
    chart.render()
    surface.write_to_png('static/img/estadisticasM.png')
    
    return render_to_response('estadisticasMaq.html', context_instance=RequestContext(request))

# ********************************* Excel *********************************
def excelRepresentantes(request):
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Listado Representantes')
    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
    header = ['Nro Legajo', 'Nombre', 'Apellido', 'DNI', 'Telefono', 'E-mail', 'Zona']
    for hcol, hcol_data in enumerate(header): # [(0,'Header 1'), (1, 'Header 2'), (2,'Header 3'), (3,'Header 4')]
            sheet.write(0, hcol, hcol_data, style=xlwt.Style.default_style)

    lista =[]
    for representante in Representante.objects.all():
        lista.append( [representante.NroLegajo,representante.Nombre, representante.Apellido,representante.DNI, representante.Telefono, representante.Email, representante.Zona] )
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
            sheet.write(i+1,j,lista[i][j],style=xlwt.Style.default_style)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Representantes.xls'
    book.save(response)
    return response

def excelProductores(request):
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Listado Productores')
    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
    header = ['CUIL', 'Nombre', 'Apellido', 'DNI', 'Telefono', 'E-mail']
    for hcol, hcol_data in enumerate(header): # [(0,'Header 1'), (1, 'Header 2'), (2,'Header 3'), (3,'Header 4')]
            sheet.write(0, hcol, hcol_data, style=xlwt.Style.default_style)
    lista =[]
    for p in Productor.objects.all():
        lista.append( [p.CUIL,p.Nombre, p.Apellido,p.DNI, p.Telefono, p.Email] )
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
            sheet.write(i+1,j,lista[i][j],style=xlwt.Style.default_style)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Productores.xls'
    book.save(response)
    return response

def excelLotes(request):
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Listado Lotes')
    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
    header = ['Nro Lote', 'Tipo Fardo', 'Cantidad Fardos', 'Peso', 'Estancia', 'Cuadricula']
    for hcol, hcol_data in enumerate(header): # [(0,'Header 1'), (1, 'Header 2'), (2,'Header 3'), (3,'Header 4')]
            sheet.write(0, hcol, hcol_data, style=xlwt.Style.default_style)
    lista =[]
    for p in Lote.objects.all():
        lista.append( [p.NroLote,p.TipoFardo.Nombre, p.CantFardos,p.Peso, p.Estancia.Nombre, p.Cuadricula] )
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
            sheet.write(i+1,j,lista[i][j],style=xlwt.Style.default_style)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Lotes.xls'
    book.save(response)
    return response

def excelFardos(request):
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Listado Fardos')
    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
    header = ['Nro Fardo', 'Nro Lote', 'Peso', 'Rinde', 'Finura', 'CV', 'Altura Media', 'Romana']
    for hcol, hcol_data in enumerate(header): # [(0,'Header 1'), (1, 'Header 2'), (2,'Header 3'), (3,'Header 4')]
            sheet.write(0, hcol, hcol_data, style=xlwt.Style.default_style)
    lista =[]
    for p in Fardo.objects.all():
        lista.append( [p.NroFardo,p.Lote.NroLote, p.Peso, p.Rinde, p.Finura, p.CV,p.AlturaMedia, p.Romana] )
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
            sheet.write(i+1,j,lista[i][j],style=xlwt.Style.default_style)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Fardos.xls'
    book.save(response)
    return response

# ********************************* LOGIN *********************************
def login_user(request):
    logout(request) # Por si un usuario se encontraba logueado
    form = LoginForm(request.POST)  
    try:
        meta = request.META['QUERY_STRING'].split('=')[1][:-1]
    except IndexError:
        meta = None
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            if meta:
                return HttpResponseRedirect(meta)
            return HttpResponseRedirect('/')
    return render(request, 'login.html', {'login_form': form })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

def recoveryPassword(request, user = None):
    logout(request) # Por si un usuario se encontraba logueado
    error = False
    try:        
        userB = User.objects.get(username = user)
    except:
        userB = None
    if userB != None:
        try:
            cont = ''.join([choice(string.letters + string.digits) for i in range(8)])
            userB.set_password(cont)
            email = EmailMessage("Recovery Password", "Mail enviado para recuperar password. You password is: " + cont, to = [userB.email])
            email.send()
            msg = 'Recovery Password, enviado a E-Mail.'
            userB.save()
            error = False
        except:
            msg = 'No se pudo recuperar password, mail incorrecto.'
            error = True
    else:
        msg = 'No se pudo recuperar password, usuario no existe.'
        error = True
        return render_to_response('recPass.html', {'msg':msg, 'error':error}, context_instance=RequestContext(request))

@login_required(login_url="/login")
def index (request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required(login_url="/login")
def acercaDe (request):
    return render_to_response('acercaDe.html', context_instance=RequestContext(request))

@login_required(login_url="/login")
def error_message (request):
    return render_to_response('403.html', context_instance=RequestContext(request))

@login_required(login_url="/login")
def error_message_404 (request):
    return render_to_response('404.html', context_instance=RequestContext(request))

# ********************************* PDF *********************************
                
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

@login_required(login_url="/login")
@permission_required('appWeb.listado_estancia', login_url='/error_message')
def pdfEstancias(request):
    estancias = Estancia.objects.all().filter(Baja = False)
    fecha = date.today()
    
    return render_to_pdf(
            'pdflistadoestancia.html',

            {   
                'pagesize':'A4',
                'lista': estancias,
                'date': fecha,    
    
            }
        )


@login_required(login_url="/login")
@permission_required('appWeb.listado_compra', login_url='/error_message')
def pdfCompras(request):
    compras = CompraLote.objects.all()
    fecha = date.today()
    return render_to_pdf(
            'pdflistadocompras.html',
            {   
                'pagesize':'A4',
                'lista': compras,
                'date': fecha,    
            }
        )

@login_required(login_url="/login")
@permission_required('appWeb.listado_productor', login_url='/error_message')
def pdfProductores(request):
    prod = Productor.objects.all().filter(Baja = False)
    fecha = date.today()
    return render_to_pdf(
            'pdflistadoproductores.html',
            {   
                'pagesize':'A4',
                'lista': prod,
                'date': fecha,    
            }
        )


@login_required(login_url="/login")
@permission_required('appWeb.listado_representante', login_url='/error_message')
def pdfRepresentantes(request):
    rep = Representante.objects.all().filter(Baja = False)
    fecha = date.today()
    
    return render_to_pdf(
            'pdflistadorepresentantes.html',
            {   
                'pagesize':'A4',
                'lista': rep,
                'date': fecha,    
            }
        )


@login_required(login_url="/login")
@permission_required('appWeb.listado_venta', login_url='/error_message')
def pdfVentas(request):
    venta = Venta.objects.all()
    fecha = date.today()
    
    return render_to_pdf(
            'pdflistadoventas.html',
            {   
                'pagesize':'A4',
                'lista': venta,
                'date': fecha,    
            }
        )

@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def pdfOp(request):
    orden = OrdenProduccion.objects.get(NroOrden = 1)
    detalles = orden.detalleorden_set   # Obtengo los detales de la orden
    nroOrden = orden.NroOrden
    fecha = date.today()
    fardosL = []
    cantidades = []
    prueba = []
    totales = []

    total_cantidad = 0
    total_peso = 0
    total_finura = 0 
    total_hm = 0
    total_cvh = 0 
    total_rinde = 0  
    total_romana = 0

    for detalle in detalles.all():                      # Recorro los detalles
        fardo = detalle.fardo_set.first()               # Obtengo el primer fardo
        cantidades.append(detalle.fardo_set.count())    # Cantidad de fardos de un detalle
        fardosL.append(fardo)                           # agrego los fardos a la lista, como 1 detalle tiene los fardos iguales,
                                                        # obtengo el primero y lo muestro en el html
        peso = detalle.fardo_set.count() * fardo.Peso

        total_cantidad = total_cantidad + detalle.fardo_set.count()
        total_peso = total_peso + (fardo.Peso*detalle.fardo_set.count())
        total_finura = total_finura + fardo.Finura
        total_hm = total_hm + fardo.AlturaMedia
        total_cvh = total_cvh + fardo.CV
        total_rinde = total_rinde + fardo.Rinde
        total_romana = total_romana + fardo.Romana
        prueba.append({'nroDetalle':detalle.NroDetalle,'estancia':fardo.Lote.Compra.Estancia.Nombre,'cantidad':detalle.fardo_set.count(),'peso':peso, 'Finura':fardo.Finura, 'HM':fardo.AlturaMedia, 'CVH':fardo.CV, 'Rinde':fardo.Rinde, 'Romana':fardo.Romana})
    if detalles.count() > 0:
        total_finura = float("%0.2f" % (total_finura / detalles.count()))
        total_hm = float("%0.2f" % (total_hm / detalles.count()))
        total_cvh = float("%0.2f" % (total_cvh / detalles.count()))
        total_rinde = float("%0.2f" % (total_rinde / detalles.count()))
        total_romana = float("%0.2f" % (total_romana / detalles.count()))

    totales.append({'total_cantidad':total_cantidad , 'total_peso':total_peso , 'total_finura':total_finura , 'total_hm':total_hm , 'total_cvh':total_cvh , 'total_rinde':total_rinde , 'total_romana':total_romana })
    return render_to_pdf(
            'pdfop.html',
            {   
                'pagesize':'A4',
                'nroOrden': nroOrden,
                'orden': orden,
                'detalles': prueba,
                'totales' : totales,
                'date': fecha,
            }
        )

# ********************************* Administracion de Compra *********************************
@login_required(login_url="/login")
@permission_required('appWeb.listado_compra', login_url='/error_message')
def listadoCompra(request):
    compra = CompraLote.objects.all()
    return render_to_response('listadoCompra.html', {'lista':compra}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_compralote', login_url='/error_message')
def registrarCompra(request):
    if request.method == 'POST':
        formulario = CompraForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoCompra')
    else:
        formulario = CompraForm()
    formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('compraForm.html', {'formulario':formulario}, context_instance=RequestContext(request))


# ********************************* Administracion de Venta *********************************
@login_required(login_url="/login")
@permission_required('appWeb.listado_venta', login_url='/error_message')
def listadoVenta(request):
    venta = Venta.objects.all()
    return render_to_response('listadoVenta.html', {'lista':venta}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_venta', login_url='/error_message')
def registrarVenta(request):
    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid():
            pk = formulario.cleaned_data['LoteVenta'].NroPartida
            loteV = LoteVenta.objects.get(pk = pk)            # Seteo la baja de lote para que no se pueda volver a cargar los fardos de ese lote
            loteV.Baja = True
            loteV.save()
            formulario.save()
            return HttpResponseRedirect('/listadoVenta')
    else:
        formulario = VentaForm()
    formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('ventaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))


# ********************************* Administracion de Estancias *********************************
@login_required(login_url="/login")
@permission_required('appWeb.listado_estancia', login_url='/error_message')
def listadoEstancias(request):
    estancia = Estancia.objects.filter(Baja = False)
    return render_to_response('listadoEstancias.html', {'lista':estancia}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_estancia', login_url='/error_message')
def registrarEstancia(request):
    if request.method == 'POST':
        formulario = EstanciaFormFactory(False)(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoEstancias')
    else:
        formulario = EstanciaFormFactory(False)()
    formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('EstanciaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.change_estancia', login_url='/error_message')
def modificarEstancia(request, pk=None):
    estancia = None
    if pk is not None:
        estancia = get_object_or_404(Estancia, pk=pk) 
    
    if request.method == 'POST':
        formulario = EstanciaFormFactory(estancia is not None)(request.POST, instance = estancia)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoEstancias')
    else:
        formulario = EstanciaFormFactory(estancia is not None)(instance = estancia)
    
    formulario.setup('Modificar', css_class="btn btn-success")
    return render_to_response('modificarEstancia.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.delete_estancia', login_url='/error_message')
def eliminarEstancia(request, pk):
    estancia = Estancia.objects.get(pk=pk)
    estancia.Baja = True
    estancia.save()
    estancia = Estancia.objects.filter(Baja = False)
    return render_to_response('listadoEstancias.html', {'lista':estancia}, context_instance=RequestContext(request))    

# ********************************* Administracion de Lotes *********************************

@login_required(login_url="/login")
@permission_required('appWeb.listado_lote', login_url='/error_message')
def listadoLotes(request):
    lote = Lote.objects.all()
    return render_to_response('listadoLotes.html', {'lista':lote}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_lote', login_url='/error_message')
def registrarLote(request, pk=None):
    lote = None
    if pk is not None:
        lote = get_object_or_404(Lote, pk=pk)

    if request.method == 'POST':

        formulario = LoteFormFactory(lote is not None)(request.POST, instance = lote)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoLotes')
    else:
        formulario = LoteFormFactory(lote is not None)(instance = lote)

    formulario.setup(pk is None and 'Registrar' or 'Modificar', css_class="btn btn-success")
    return render_to_response('registrarLoteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.delete_lote', login_url='/error_message')
def eliminarLoteId(request, pk):
    lote = Lote.objects.get(pk=pk)
    lote.Baja = True
    lote.save()
    lote = Lote.noEliminados.all()
    return render_to_response('listadoLotes.html', {'lista':lote}, context_instance=RequestContext(request))    

# ********************************* Administracion de Fardos *********************************

@login_required(login_url="/login")
@permission_required('appWeb.listado_fardo', login_url='/error_message')
def listadoFardos(request):
    fardo = Fardo.objects.all()
    return render_to_response('listadoFardos.html', {'lista':fardo}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_fardo', login_url='/error_message')
def registrarFardo(request, pk=None):
    fardo = None
    if pk is not None:
        fardo = get_object_or_404(Fardo, pk=pk)

    if request.method == 'POST':
        formulario = FardoFormFactory(fardo is not None)(request.POST, instance = fardo) 
        if formulario.is_valid():
            if pk is None:
                for x in xrange(formulario.cleaned_data['Lote'].CantFardos): # Segun la cantidad de fardos en lote, son las instancia que creo
                    Fardo.objects.create(Lote = formulario.cleaned_data['Lote'], Peso = (formulario.cleaned_data['Lote'].Peso / formulario.cleaned_data['Lote'].CantFardos),
                                        Rinde = formulario.cleaned_data['Rinde'], Finura = formulario.cleaned_data['Finura'],
                                        CV = formulario.cleaned_data['CV'], AlturaMedia = formulario.cleaned_data['AlturaMedia'],
                                        Romana = formulario.cleaned_data['Romana'])
            else:
                formulario = FardoFormFactory(fardo is not None)(request.POST, instance = fardo)  # Modifico todos los fardos del mismo lote al modificar uno
                formulario.save()

            return HttpResponseRedirect('/listadoFardos')
    else:
        formulario = FardoFormFactory(fardo is not None)(instance = fardo)

    formulario.setup(pk is None and 'Registrar' or 'Modificar', css_class="btn btn-success")
    return render_to_response('registrarFardoForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

# ********************************* Administracion de Productor *********************************
    
@login_required(login_url="/login")
@permission_required('appWeb.listado_productor', login_url='/error_message')
def listadoProductores(request):
    productor = Productor.objects.filter(Baja = False)
    return render_to_response('listadoProductores.html', {'lista':productor}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_productor', login_url='/error_message')
def registrarProductor(request):
    if request.method == 'POST':
        formulario = ProductorFormFactory(False)(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoProductores')
    else:
        formulario = ProductorFormFactory(False)()
    formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('ProductorForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.change_productor', login_url='/error_message')
def modificarProductor(request, pk=None):
    productor = None
    if pk is not None:
        productor = get_object_or_404(Productor, pk=pk)
    if request.method == 'POST':
        formulario = ProductorFormFactory(True)(request.POST, instance = productor)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoProductores')
    else:
        formulario = ProductorFormFactory(True)(instance = productor)
    
    formulario.setup('Modificar', css_class="btn btn-success")
    return render_to_response('modificarProductor.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.delete_productor', login_url='/error_message')
def eliminarProductor(request,pk):
    productor = Productor.objects.get(pk=pk)
    productor.Baja = True
    productor.save()
    productor = Productor.objects.filter(Baja = False)
    return render_to_response('listadoProductores.html', {'lista':productor}, context_instance=RequestContext(request))

# ********************************* Administracion de Representante *********************************

@login_required(login_url="/login")
@permission_required('appWeb.listado_representante', login_url='/error_message')
def listadoRepresentante(request):
    representante = Representante.objects.filter(Baja = False)
    return render_to_response('listadoRepresentante.html', {'lista':representante}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_representante', login_url='/error_message')
def registrarRepresentante(request):
    if request.method == 'POST':
        formulario = RepresentanteFormFactory(False)(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoRepresentante')
    else:
        formulario = RepresentanteFormFactory(False)()
    formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('RepresentanteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.change_representante', login_url='/error_message')
def modificarRepresentante(request, pk=None):
    representante = None
    if pk is not None:
        representante = get_object_or_404(Representante, pk=pk) 
    if request.method == 'POST':
        formulario = RepresentanteFormFactory(True)(request.POST, instance = representante)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoRepresentante')
    else:
        formulario = RepresentanteFormFactory(True)(instance = representante)
    
    formulario.setup('Modificar', css_class="btn btn-success")
    return render_to_response('modificarRepresentante.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.delete_representante', login_url='/error_message')
def eliminarRepresentante(request,pk):
    representante = Representante.objects.get(pk=pk)
    representante.Baja = True
    representante.save()
    representante = Representante.objects.filter(Baja = False)
    return render_to_response('listadoRepresentante.html', {'lista':representante}, context_instance=RequestContext(request))

# ********************************* Administracion de Produccion *********************************

@login_required(login_url="/login")
@permission_required('appWeb.listado_orden', login_url='/error_message')
def listadoOrden(request):
    op = OrdenProduccion.objects.filter(Cancelada = False)
    return render_to_response('listadoOrden.html', {'lista':op}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def registrarOrdenProduccion(request, pk=None):
    orden = None
    serv = []       # Arreglo de servicios para almacenar los que ingreso.

    if pk is not None:
        orden = get_object_or_404(OrdenProduccion, pk=pk)

    if request.method == 'POST':
        formulario = OrdenProduccionFormFactory(orden is not None)(request.POST, instance = orden)
        if formulario.is_valid():
            orden = formulario.save()
            return HttpResponseRedirect('/listadoOrden')
    else:
        formulario = OrdenProduccionFormFactory(orden is not None)(instance = orden)
        
    formulario.setup(pk is None and 'Registrar' or 'Modificar', css_class="btn btn-success")
    return render_to_response('OrdenProduccionForm.html', {'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url="/login")
@permission_required('appWeb.change_ordenproduccion', login_url='/error_message')
def modificarOrdenProduccion(request, pk=None):
    orden = None
    serv = []       # Arreglo de servicios para almacenar los que ingreso.

    if pk is not None:
        orden = get_object_or_404(OrdenProduccion, pk=pk)

    if request.method == 'POST':
        formulario = OrdenProduccionFormFactory(orden is not None)(request.POST, instance = orden)
        if formulario.is_valid():
            orden = formulario.save()
            return HttpResponseRedirect('/listadoOrden')
    else:
        formulario = OrdenProduccionFormFactory(orden is not None)(instance = orden)
        
    formulario.setup('Modificar', css_class="btn btn-success")
    return render_to_response('modificarOrdenProduccion.html', {'formulario':formulario}, context_instance=RequestContext(request))



@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def verOrdenProduccion(request, pk):
    orden = OrdenProduccion.objects.get(NroOrden = pk)
    detalles = orden.detalleorden_set   # Obtengo los detales de la orden

    fardosL = []
    cantidades = []
    prueba = []
    totales = []

    total_cantidad = 0
    total_peso = 0
    total_finura = 0 
    total_hm = 0
    total_cvh = 0 
    total_rinde = 0  
    total_romana = 0

    for detalle in detalles.all():                      # Recorro los detalles
        fardo = detalle.fardo_set.first()               # Obtengo el primer fardo
        cantidades.append(detalle.fardo_set.count())    # Cantidad de fardos de un detalle
        fardosL.append(fardo)                           # agrego los fardos a la lista, como 1 detalle tiene los fardos iguales,
                                                        # obtengo el primero y lo muestro en el html
        peso = detalle.fardo_set.count() * fardo.Peso

        total_cantidad = total_cantidad + detalle.fardo_set.count()
        total_peso = total_peso + (fardo.Peso*detalle.fardo_set.count())
        total_finura = total_finura + fardo.Finura
        total_hm = total_hm + fardo.AlturaMedia
        total_cvh = total_cvh + fardo.CV
        total_rinde = total_rinde + fardo.Rinde
        total_romana = total_romana + fardo.Romana

        prueba.append({'nroDetalle':detalle.NroDetalle,'estancia':fardo.Lote.Compra.Estancia.Nombre,'cantidad':detalle.fardo_set.count(),'peso':peso, 'Finura':fardo.Finura, 'HM':fardo.AlturaMedia, 'CVH':fardo.CV, 'Rinde':fardo.Rinde, 'Romana':fardo.Romana})

    if detalles.count() > 0:
        total_finura = float("%0.2f" % (total_finura / detalles.count()))
        total_hm = float("%0.2f" % (total_hm / detalles.count()))
        total_cvh = float("%0.2f" % (total_cvh / detalles.count()))
        total_rinde = float("%0.2f" % (total_rinde / detalles.count()))
        total_romana = float("%0.2f" % (total_romana / detalles.count()))


    totales.append({'total_cantidad':total_cantidad , 'total_peso':total_peso , 'total_finura':total_finura , 'total_hm':total_hm , 'total_cvh':total_cvh , 'total_rinde':total_rinde , 'total_romana':total_romana })
    
    return render_to_response('datosOrden.html', {'orden':orden, 'detalles':prueba, 'totales':totales}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def mostrarEstancia (request, pk):
    orden = OrdenProduccion.objects.get(NroOrden = pk)
    est = [] # Estancia que tiene fardos con especificaciones requeridas

    for estancia in Estancia.objects.all():
        lotes = estancia.lote_set.all()
        for lote in lotes:
            if lote.fardo_set.filter(CV__range = (orden.CV - ((orden.CV * Config.objects.get_int('CV_%_OK')) / 100), orden.CV + ((orden.CV * Config.objects.get_int('CV_%_OK')) / 100)), 
                                        AlturaMedia__range = (orden.AlturaMedia - ((orden.AlturaMedia * Config.objects.get_int('ALTURAMEDIA_%_OK')) / 100), orden.AlturaMedia + ((orden.AlturaMedia * Config.objects.get_int('ALTURAMEDIA_%_OK')) / 100)), 
                                        Finura__range = (orden.Finura - ((orden.Finura * Config.objects.get_int('FINURA_%_OK')) / 100), orden.Finura + ((orden.Finura * Config.objects.get_int('FINURA_%_OK')) / 100)), 
                                        Romana__range = (orden.Romana - ((orden.Romana * Config.objects.get_int('ROMANA_%_OK')) / 100), orden.Romana + ((orden.Romana * Config.objects.get_int('ROMANA_%_OK')) / 100)), 
                                        Rinde__range = (orden.Rinde - ((orden.Rinde * Config.objects.get_int('RINDE_%_OK')) / 100), orden.Rinde + ((orden.Rinde * Config.objects.get_int('RINDE_%_OK')) / 100)), 
                                        DetalleOrden = None):

                est.append(estancia)
                break

    return render_to_response('OrdenProduccion/agregarDetalle.html', {'estancias':est, 'orden':orden}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def mostrarLotes (request, estancia, orden):
    
    orden = OrdenProduccion.objects.get(NroOrden = orden)
    estancia = Estancia.objects.get( CUIT = estancia )

    lotes = [] # Lotes que tienen fardos con especificaciones requeridas
    fardos = [] # datos de fardo
    for lote in estancia.lote_set.all():
        if lote.fardo_set.filter(CV__range = (orden.CV - ((orden.CV * Config.objects.get_int('CV_%_OK')) / 100), orden.CV + ((orden.CV * Config.objects.get_int('CV_%_OK')) / 100)), 
                                        AlturaMedia__range = (orden.AlturaMedia - ((orden.AlturaMedia * Config.objects.get_int('ALTURAMEDIA_%_OK')) / 100), orden.AlturaMedia + ((orden.AlturaMedia * Config.objects.get_int('ALTURAMEDIA_%_OK')) / 100)), 
                                        Finura__range = (orden.Finura - ((orden.Finura * Config.objects.get_int('FINURA_%_OK')) / 100), orden.Finura + ((orden.Finura * Config.objects.get_int('FINURA_%_OK')) / 100)), 
                                        Romana__range = (orden.Romana - ((orden.Romana * Config.objects.get_int('ROMANA_%_OK')) / 100), orden.Romana + ((orden.Romana * Config.objects.get_int('ROMANA_%_OK')) / 100)), 
                                        Rinde__range = (orden.Rinde - ((orden.Rinde * Config.objects.get_int('RINDE_%_OK')) / 100), orden.Rinde + ((orden.Rinde * Config.objects.get_int('RINDE_%_OK')) / 100)), 
                                        DetalleOrden = None):
            lotes.append(lote)
            fardos.append(lote.fardo_set.first())
            continue

    data1 =serializers.serialize('json', fardos) 
    data = serializers.serialize('json', lotes)
    
    return HttpResponse(json.dumps({'lotes':data, 'fardos':data1}), content_type='json')
    
@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def mostrarFardos (request, pk):
    lote = Lote.objects.get( NroLote = pk )
    
    fardos_set = lote.fardo_set
    fardos = fardos_set.all().filter(DetalleOrden = None)
    data = serializers.serialize('json', fardos)
    return HttpResponse(data, content_type='json')    

@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def agregarDetalle (request, campos = None, orden = None): # En caso de que todos los fardos que eligio se pasen de
                                                           # la cantidad requerida solo tomara los fardos que aproximen
                                                           # ese valor
    kgInOrden = 0               # Guardo los kilos que voy llenando en la orden
    kgAgregados = 0
    detalle = DetalleOrden()
    ordenKg = OrdenProduccion.objects.get(NroOrden = orden)
    detalle.OrdenProduccion = ordenKg
    detalle.save()

    campos = campos.split(",")

    for campo in campos:
        ordenKg = OrdenProduccion.objects.get(NroOrden = orden)
        for d in ordenKg.detalleorden_set.all():    # Obtengo todo el peso de la orden por los detalles
            for f in d.fardo_set.all():
                kgInOrden = f.Peso + kgInOrden

        if campo != ',':
            fardo = Fardo.objects.get(NroFardo = int(campo))
            if ordenKg.CantRequerida > kgInOrden:      # Si necesito mas fardo lo agrego
                fardo.DetalleOrden = detalle
                fardo.save()
                kgAgregados = kgAgregados + fardo.Peso
            else: 
                break

        kgInOrden = 0    
    

    return HttpResponse(json.dumps({'kg': kgAgregados}), content_type="application/json")   

@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def cancelarOrdenProduccion(request, pk):
    orden = OrdenProduccion.objects.get( NroOrden=pk )
    orden.Cancelada = True
    
    for detalle in orden.detalleorden_set.all():
        for fardo in detalle.fardo_set.all():
            fardo.DetalleOrden = None
            fardo.save()
        detalle.delete()

    orden.save()
    return HttpResponseRedirect('/listadoOrden')    
    
@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def enviarFaseProduccion(request, pk):
    maq = []
    orden = OrdenProduccion.objects.get(NroOrden = pk)
    for p in orden.produccion_set.all():
        if p.FechaInicio == None:
            maquinaria = Maquinaria.objects.filter(Servicio = p.Servicio, Baja = False)
            break
    for m in maquinaria:
        if m.isLibre():
            maq.append(m)

    return render_to_response('enviarFaseProduccionForm.html', {'orden':orden, 'maquinaria':maq}, context_instance=RequestContext(request))
    

@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def commitIniciarFase(request, orden, nroSerie):
    o = OrdenProduccion.objects.get(NroOrden = orden)
    m = Maquinaria.objects.get(NroSerie = nroSerie)

    for p in o.produccion_set.all():
        if p.FechaInicio == None:
            p.FechaInicio = datetime.today()
            p.Maquinaria = m
            p.save()
            break

    return HttpResponseRedirect('/listadoOrden')    

@login_required(login_url="/login")
@permission_required('appWeb.add_ordenproduccion', login_url='/error_message')
def finalizarFaseProduccion(request, pk):
    orden = OrdenProduccion.objects.get(NroOrden = pk)
    for p in orden.produccion_set.all():
        if p.FechaInicio != None and p.FechaFin == None:
            p.FechaFin = datetime.today()
            p.save()
            break

    return HttpResponseRedirect('/listadoOrden')    

# ********************************* Administracion de Lote de Ventas *********************************

@login_required(login_url="/login")
@permission_required('appWeb.add_loteventa', login_url='/error_message')
def commitLoteVenta(request, cuadricula = None, orden = None):
    o = OrdenProduccion.objects.get(NroOrden = orden)
    v = LoteVenta()
    v.OrdenProduccion = o
    v.Cantidad = o.CantRequerida
    v.Cuadricula = cuadricula
    v.save()
        
    return HttpResponseRedirect('/listadoOrden') 

@login_required(login_url="/login")
@permission_required('appWeb.add_loteventa', login_url='/error_message')
def agregarLoteVenta(request, pk):
    o = OrdenProduccion.objects.get(NroOrden = pk)
    return render_to_response('LoteVentaForm.html', {'orden':o}, context_instance=RequestContext(request))

# ********************************* Administracion de Maquinarias *********************************

@login_required(login_url="/login")
@permission_required('appWeb.listado_maquinaria', login_url='/error_message')
def listadoMaquinaria(request):
    maquinaria = Maquinaria.objects.filter(Baja = False)
    return render_to_response('listadoMaquinaria.html', {'lista':maquinaria}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.add_maquinaria', login_url='/error_message')
def registrarMaquinaria(request):
    if request.method == 'POST':
        formulario = MaquinariaFormFactory(False)(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoMaquinaria')
    else:
        formulario = MaquinariaFormFactory(False)() 
    formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('MaquinariaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.change_maquinaria', login_url='/error_message')
def modificarMaquinaria(request, pk=None):
    maquinaria = None
    if pk is not None:
        maquinaria = get_object_or_404(Maquinaria, pk=pk) 
    
    if request.method == 'POST':
        formulario = MaquinariaFormFactory(maquinaria is not None)(request.POST, instance = maquinaria)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoMaquinaria')
    else:
        formulario = MaquinariaFormFactory(maquinaria is not None)(instance = maquinaria)
    
    formulario.setup('Modificar', css_class="btn btn-success")
    return render_to_response('modificarMaquinaria.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.delete_maquinaria', login_url='/error_message')
def eliminarMaquinaria(request,pk):
    maquinaria = Maquinaria.objects.get(pk=pk)    
    maquinaria.Baja = True
    maquinaria.save()
    maquinaria = Maquinaria.objects.filter(Baja = False)
    return render_to_response('listadoMaquinaria.html', {'lista':maquinaria}, context_instance=RequestContext(request))

# ********************************* Busquedas por Criterio *********************************

@login_required(login_url="/login")
@permission_required('appWeb.listado_compra', login_url='/error_message')
def buscarCompra(request, pkb):
    total = 0
    results = []
    
    if not pkb:
        return render_to_response("listadoCompra.html", { "lista": Compra.objects.all() }, context_instance=RequestContext(request))
    
    if pkb.isdigit():
        results4 = CompraLote.objects.all().filter(NroCompra = pkb)
        for obj in results4:
            results.append(obj)

    representante = Representante.objects.all().filter(Nombre = pkb)
    representante2 = Representante.objects.all().filter(Apellido = pkb)
    results1 = CompraLote.objects.all().filter(Representante = representante)
    results2 = CompraLote.objects.all().filter(Representante = representante2)
    
    estancia = Estancia.objects.all().filter(Nombre = pkb)
    results3 = CompraLote.objects.all().filter(Estancia = estancia)
    
    for obj in results1:
        results.append(obj)
        total = total + 1
    for obj in results3:
        results.append(obj)



 
    return render_to_response("listadoCompra.html", { "lista": results }, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.listado_venta', login_url='/error_message')
def buscarVenta(request, pkb):
    results = []
    if pkb.isdigit():
        results1 = Venta.objects.all().filter(NroVenta = pkb)

        for obj in results1:
            results.append(obj)
     
    return render_to_response("listadoVenta.html", { "lista": results }, context_instance=RequestContext(request))


@login_required(login_url="/login")
@permission_required('appWeb.listado_estancia', login_url='/error_message')
def buscarEstancia(request, pkb):
    results = []

    results1 = Estancia.objects.all().filter(CUIT = pkb)
    results2 = Estancia.objects.all().filter(Nombre = pkb)

    for obj in results1:
        results.append(obj)
    for obj in results2:
        results.append(obj)    
 
    return render_to_response("listadoEstancias.html", { "lista": results }, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.listado_lote', login_url='/error_message')
def buscarLote(request, pkb):
    results = []
    if pkb.isdigit():
        results2 = Lote.objects.all().filter(NroLote = pkb)
        for obj in results2:
            results.append(obj)

    return render_to_response("listadoLotes.html", { "lista": results }, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.listado_fardo', login_url='/error_message')
def buscarFardo(request, pkb):
    results = []
    if pkb.isdigit():
        results1 = Fardo.objects.all().filter(NroFardo = pkb)

        for obj in results1:
            results.append(obj)
 
    return render_to_response("listadoFardos.html", { "lista": results }, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.listado_productor', login_url='/error_message')
def buscarProductor(request, pkb):
    results = []

    results1 = Productor.objects.all().filter(Nombre = pkb)
    results2 = Productor.objects.all().filter(DNI = pkb)
    results3 = Productor.objects.all().filter(Apellido = pkb)

    for obj in results1:
        results.append(obj)
    for obj in results2:
        results.append(obj)
    for obj in results3:
        results.append(obj)

    return render_to_response("listadoProductores.html", { "lista": results }, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.listado_representante', login_url='/error_message')
def buscarRepresentante(request, pkb):
    results = []

    results1 = Representante.objects.all().filter(Nombre = pkb)
    results2 = Representante.objects.all().filter(Apellido = pkb)
    results3 = Representante.objects.all().filter(DNI = pkb)

    for obj in results1:
        results.append(obj)
    for obj in results2:
        results.append(obj)
    for obj in results3:
        results.append(obj)

    return render_to_response("listadoRepresentante.html", { "lista": results }, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.listado_orden', login_url='/error_message')
def buscarOrden(request, pkb):
    results = []

    if pkb.isdigit():
        results1 = OrdenProduccion.objects.all().filter(NroOrden = pkb)

        for obj in results1:
            results.append(obj)
 
    return render_to_response("listadoOrden.html", { "lista": results }, context_instance=RequestContext(request))

@login_required(login_url="/login")
@permission_required('appWeb.listado_maquinaria', login_url='/error_message')
def buscarMaquinaria(request, pkb):
    results = []
    results1 = Maquinaria.objects.all().filter(Servicio = pkb)
        
    for obj in results1:
        results.append(obj)

    return render_to_response("listadoMaquinaria.html", { "lista": results }, context_instance=RequestContext(request))