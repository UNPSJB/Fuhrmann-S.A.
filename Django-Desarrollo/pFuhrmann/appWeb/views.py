import urlparse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from appWeb.models import *
from appWeb.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import (REDIRECT_FIELD_NAME, login, logout, authenticate)
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def index (request):
    return render_to_response('index.html', context_instance=RequestContext(request))

# --------------- Administracion de Compra

def listadoCompra(request):
    compra = CompraLote.objects.all()
    return render_to_response('listadoCompra.html', {'lista':compra}, context_instance=RequestContext(request))

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

# --------------- Administracion de Venta

def listadoVenta(request):
    venta = Venta.objects.all()
    return render_to_response('listadoVenta.html', {'lista':venta}, context_instance=RequestContext(request))

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

# --------------- Administracion de Estancias

def listadoEstancias(request):
    estancia = Estancia.objects.all()
    return render_to_response('listadoEstancias.html', {'lista':estancia}, context_instance=RequestContext(request))

def registrarEstancia(request):
    if request.method == 'POST':
        formulario = EstanciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoEstancias')
    else:
        formulario = EstanciaForm()
    formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('EstanciaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarEstancia(request, pk=None):
    estancia = None
    if pk is not None:
        estancia = get_object_or_404(Estancia, pk=pk) 
    if request.method == 'POST':
        formulario = EstanciaForm(request.POST, instance=estancia)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoEstancias')
    else:
        formulario = EstanciaForm(instance = estancia)
    formulario.setup(pk is None and 'Registrar' or 'Modificar', css_class="btn btn-success")
    return render_to_response('EstanciaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarEstancia(request, pk):
    estancia = Estancia.objects.get(pk=pk)
    estancia.delete()
    estancia = Estancia.objects.all()
    return render_to_response('listadoEstancias.html', {'lista':estancia}, context_instance=RequestContext(request))    

# --------------- Administracion de Lotes

def listadoLotes(request):
    lote = Lote.objects.all()
    return render_to_response('listadoLotes.html', {'lista':lote}, context_instance=RequestContext(request))

def registrarLote(request, pk=None):
    lote = None
    if pk is not None:
        lote = get_object_or_404(Lote, pk=pk)

    if request.method == 'POST':
        formulario = LoteForm(request.POST, instance = lote)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoLotes')
    else:
        formulario = LoteForm(instance = lote)

    formulario.setup(pk is None and 'Registrar' or 'Modificar', css_class="btn btn-success")
    return render_to_response('registrarLoteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarLoteId(request, pk):
    lote = Lote.objects.get(pk=pk)
    lote.Baja = True
    lote.save()
    lote = Lote.objects.all()
    return render_to_response('listadoLotes.html', {'lista':lote}, context_instance=RequestContext(request))    

# --------------- Administracion de Fardos

def listadoFardos(request):
    fardo = Fardo.objects.all()
    return render_to_response('listadoFardos.html', {'lista':fardo}, context_instance=RequestContext(request))

def registrarFardo(request, pk=None):
    fardo = None
    if pk is not None:
        fardo = get_object_or_404(Fardo, pk=pk)

    if request.method == 'POST':
        formulario = FardoForm(request.POST, instance = fardo)
        if formulario.is_valid():
            pk1 = formulario.cleaned_data['Lote'].NroLote

            if pk1 is not None:
                for x in xrange(formulario.cleaned_data['Lote'].CantFardos): # Segun la cantidad de fardos en lote, son las instancia que creo
                    formulario.save()
                    formulario = FardoForm(request.POST)
                
                lote = Lote.objects.get(pk = pk1)            # Seteo la baja de lote para que no se pueda volver a cargar los fardos de ese lote
                lote.Baja = True
            else:
                lote_id = fardo.Lote_id                     # obtener el lote asociado
                l = Lote.objects.get(NroLote = lote_id )    # Obtener el lote con id = lote_id 
                f_set = l.fardo_set                         # obtener todos los fardos asociados al lote obtenido antes
                                
                for f in f_set.all():                       # Coleccion de fardos
                    formulario = FardoForm(request.POST, instance = f)  # Modifico todos los fardos del mismo lote al modificar uno
                    formulario.save()

            return HttpResponseRedirect('/listadoFardos')
    else:
        formulario = FardoForm(instance = fardo)

    formulario.setup(pk is None and 'Registrar' or 'Modificar', css_class="btn btn-success")
    return render_to_response('registrarFardoForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

# --------------- Administracion de Productor
    
def listadoProductores(request):
    productor = Productor.objects.all()
    return render_to_response('listadoProductores.html', {'lista':productor}, context_instance=RequestContext(request))

def registrarProductor(request):
    if request.method == 'POST':
        formulario = ProductorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoProductores')
    else:
        formulario = ProductorForm()
        formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('ProductorForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarProductor(request, pk=None):
    productor = None
    if pk is not None:
        productor = get_object_or_404(Productor, pk=pk) 
    if request.method == 'POST':
        formulario = ProductorForm(request.POST, instance=productor)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoProductores')
    else:
        formulario = ProductorForm(instance = productor)
    formulario.setup(pk is None and 'Registrar' or 'Modificar', css_class="btn btn-success")
    return render_to_response('ProductorForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarProductor(request,pk):
    productor = Productor.objects.get(pk=pk)
    productor.delete()
    productor = Productor.objects.all()
    return render_to_response('listadoProductores.html', {'lista':productor}, context_instance=RequestContext(request))

#-----------Administracion de Representante

def listadoRepresentante(request):
    representante = Representante.objects.all()
    return render_to_response('listadoRepresentante.html', {'lista':representante}, context_instance=RequestContext(request))

def registrarRepresentante(request):
    if request.method == 'POST':
        formulario = RepresentanteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoRepresentante')
    else:
        formulario = RepresentanteForm()
        formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('RepresentanteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarRepresentante(request, pk=None):
    representante = None
    if pk is not None:
        representante = get_object_or_404(Representante, pk=pk) 
    if request.method == 'POST':
        formulario = RepresentanteForm(request.POST, instance=representante)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoRepresentante')
    else:
        formulario = RepresentanteForm(instance = representante)
    formulario.setup(pk is None and 'Registrar' or 'Modificar', css_class="btn btn-success")
    return render_to_response('RepresentanteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarRepresentante(request,pk):
    representante = Representante.objects.get(pk=pk)
    representante.delete()
    representante = Representante.objects.all()
    return render_to_response('listadoRepresentante.html', {'lista':representante}, context_instance=RequestContext(request))

# --------------- Administracion de Produccion

def listadoOrden(request):
    op = OrdenProduccion.objects.all()
    return render_to_response('listadoOrden.html', {'lista':op}, context_instance=RequestContext(request))

def registrarOrdenProduccion(request):
    if request.method == 'POST':
        formulario = OrdenProduccionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoOrden')
    else:
        formulario = OrdenProduccionForm()
        formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('OrdenProduccionForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    
def modificarOrdenProduccion(request, pk):
    if request.method == 'POST':
        formulario = OrdenProduccionForm(request.POST, instance = op)
        if formulario.is_valid():
            if OrdenProduccion.EnProduccion == True:  
                formulario.save()
                formulario = OrdenProduccionForm(instance= op)
                formulario.setup('Modificar', css_class="btn btn-success")
                return HttpResponseRedirect('/listadoOrden')
    return render_to_response('modificarOrdenProduccion.html', {'formulario':formulario}, context_instance=RequestContext(request))

def cancelarOrdenProduccion(request):
    orden = OrdenProduccion.objects.all()
    return render_to_response('cancelarOrdenProduccionForm.html', {'lista':orden}, context_instance=RequestContext(request))
    
def enviarFaseProduccion(request):
    orden = OrdenProduccion.objects.all()
    return render_to_response('enviarFaseProduccionForm.html', {'lista':orden}, context_instance=RequestContext(request))
    
def finalizarFaseProduccion(request):
    orden = OrdenProduccion.objects.all()
    return render_to_response('finalizarFaseProduccionForm.html', {'lista':orden}, context_instance=RequestContext(request))   

#-----------Administracion de Maquinarias  

def listadoMaquinaria(request):
    maquinaria = Maquinaria.objects.all()
    return render_to_response('listadoMaquinaria.html', {'lista':maquinaria}, context_instance=RequestContext(request))

def registrarMaquinaria(request):
    if request.method == 'POST':
        formulario = MaquinariaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/listadoMaquinaria')
    else:
        formulario = MaquinariaForm()
        formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('MaquinariaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarMaquinaria(request,pk):
    maquinaria = Maquinaria.objects.get(pk=pk)    
    maquinaria.delete()
    maquinaria = Maquinaria.objects.all()
    return render_to_response('listadoMaquinaria.html', {'lista':maquinaria}, context_instance=RequestContext(request))