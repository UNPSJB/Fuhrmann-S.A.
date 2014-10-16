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


def index (request):
    return render_to_response('index.html', context_instance=RequestContext(request))


# Funciones para crear formularios
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
            formulario.save()
            return HttpResponseRedirect('/listadoVenta')
    else:
        formulario = ventaForm()
        formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('ventaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

#ORDEN DE PRODUCCION
def nuevaOrdenProduccion(request):
    if request.method == 'POST':
        formulario = nuevaOrdenProduccionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/nuevaOrdenProduccion')
    else:
        formulario = nuevaOrdenProduccionForm()
    return render_to_response('nuevaOrdenProduccionForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def listadoOrden(request):
    op = OrdenProduccion.objects.all()
    return render_to_response('listadoOrden.html', {'lista':op}, context_instance=RequestContext(request))

def modificarOrdenProduccion(request):
    orden = OrdenProduccion.objects.all()
    return render_to_response('modificarOrdenProduccion.html', {'lista':orden}, context_instance=RequestContext(request))
    
def modificarOrdenProduccionF(request):
    if request.method == 'POST':
        formulario = modificarOrdenProduccionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarOrdenProduccionF')
    else:
        formulario = modificarOrdenProduccionForm()
    return render_to_response('modificarOrdenProduccionForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    
def cancelarOrdenProduccion(request):
    orden = OrdenProduccion.objects.all()
    return render_to_response('cancelarOrdenProduccionForm.html', {'lista':orden}, context_instance=RequestContext(request))
    
def enviarFaseProduccion(request):
    orden = OrdenProduccion.objects.all()
    return render_to_response('enviarFaseProduccionForm.html', {'lista':orden}, context_instance=RequestContext(request))
    
def finalizarFaseProduccion(request):
    orden = OrdenProduccion.objects.all()
    return render_to_response('finalizarFaseProduccionForm.html', {'lista':orden}, context_instance=RequestContext(request))   

#LOTES
def registrarLote(request):
    if request.method == 'POST':
        formulario = registrarLoteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarLote')
    else:
        formulario = registrarLoteForm()
    return render_to_response('registrarLoteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarLote(request):
    lote = Lote.objects.all()   
    return render_to_response('modificarLote.html', {'lista':lote}, context_instance=RequestContext(request))

def modificarLoteF(request, pk):
    lote = Lote.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = modificarLoteForm(request.POST, instance = lote)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarLoteF')
    else:
        formulario = modificarLoteForm(instance = lote)
    return render_to_response('modificarLoteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarLoteId(request, pk):
    lote = Lote.objects.get(pk=pk)
    lote.Baja = True
    lote.save()
    lote = Lote.objects.all()
    return render_to_response('modificarLote.html', {'lista':lote}, context_instance=RequestContext(request))    

def listadoLotes(request):
    lote = Lote.objects.all()
    return render_to_response('listadoLotes.html', {'lista':lote}, context_instance=RequestContext(request))

#FARDOS
def registrarFardo(request):
    if request.method == 'POST':
        formulario = registrarFardoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarFardo')
    else:
        formulario = registrarFardoForm()
    return render_to_response('registrarFardoForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarFardo(request):
    fardo = Fardo.objects.all()
    return render_to_response('modificarFardo.html', {'lista':fardo}, context_instance=RequestContext(request))
    
def modificarFardoF(request):
    if request.method == 'POST':
        formulario = modificarFardoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarFardoF')
    else:
        formulario = modificarFardoForm()
    return render_to_response('modificarFardoForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    
def listadoFardos(request):
    fardo = Fardo.objects.all()
    return render_to_response('listadoFardos.html', {'lista':fardo}, context_instance=RequestContext(request))

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
    return render_to_response('registrarEstanciaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

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
    return render_to_response('registrarEstanciaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarEstancia(request, pk):
    estancia = Estancia.objects.get(pk=pk)
    estancia.delete()
    estancia = Estancia.objects.all()
    return render_to_response('listadoEstancias.html', {'lista':estancia}, context_instance=RequestContext(request))    

#PRODUCTOR
def registrarProductor(request):
    if request.method == 'POST':
        formulario = ProductorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarProductor')
    else:
        formulario = ProductorForm()
        formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('ProductorForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarProductor(request):
    productores = Productor.objects.all()
    return render_to_response('modificarProductor.html', {'lista':productores}, context_instance=RequestContext(request))
    
def modificarProductorF(request,pk):
    productor = Productor.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = modificarProductorForm(request.POST, instance=productor)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarProductorF')
    else:
        formulario = modificarProductorForm(instance=productor)
    return render_to_response('modificarProductorForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarProductor(request,pk):
    productor = Productor.objects.get(pk=pk)
    productor.delete()
    productor = Productor.objects.all()
    return render_to_response('listadoProductores.html', {'lista':productor}, context_instance=RequestContext(request))
    
def listadoProductores(request):
    productor = Productor.objects.all()
    return render_to_response('listadoProductores.html', {'lista':productor}, context_instance=RequestContext(request))

#REPRESENTANTE
def listadoRepresentante(request):
    representante = Representante.objects.all()
    return render_to_response('listadoRepresentante.html', {'lista':representante}, context_instance=RequestContext(request))

def registrarRepresentante(request):
    if request.method == 'POST':
        formulario = registrarRepresentanteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarRepresentante')
    else:
        formulario = registrarRepresentanteForm()
        formulario.setup('Registrar', css_class="btn btn-success")
    return render_to_response('registrarRepresentanteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarRepresentante(request):
    representantes = Representante.objects.all()
    return render_to_response('modificarRepresentante.html', {'lista':representantes}, context_instance=RequestContext(request))
    
def modificarRepresentanteF(request,pk):
    representante = Representante.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = modificarRepresentanteForm(request.POST, intance=representante)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarRepresentanteF')
    else:
        formulario = modificarRepresentanteForm(instance=representante)
    return render_to_response('modificarRepresentanteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    
def eliminarRepresentante(request,pk):
    representante = Representante.objects.get(pk=pk)
    representante.delete()
    representante = Representante.objects.all()
    return render_to_response('listadoRepresentante.html', {'lista':representante}, context_instance=RequestContext(request))


#-----------Administracion de Maquinarias    
def listadoMaquinaria(request):
    maquinaria = Maquinaria.objects.all()
    return render_to_response('listadoMaquinaria.html', {'lista':maquinaria}, context_instance=RequestContext(request))

def registrarMaquinaria(request):
    if request.method == 'POST':
        formulario = registrarMaquinariaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarMaquinaria')
    else:
        formulario = registrarMaquinariaForm()
    return render_to_response('registrarMaquinariaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarMaquinaria(request):
    maquinaria = Maquinaria.objects.all()
    return render_to_response('modificarMaquinaria.html', {'lista':maquinaria}, context_instance=RequestContext(request))
    
def modificarMaquinariaF(request, pk):
    maquinaria = Maquinaria.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = modificarMaquinariaForm(request.POST, instance = maquinaria)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarMaquinariaF')
    else:
        formulario = modificarMaquinariaForm(instance = maquinaria)
    return render_to_response('modificarMaquinariaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def eliminarMaquinaria(request,pk):
    maquinaria = Maquinaria.objects.get(pk=pk)    
    maquinaria.delete()
    maquinaria = Maquinaria.objects.all()
    return render_to_response('listadoMaquinaria.html', {'lista':maquinaria}, context_instance=RequestContext(request))        
