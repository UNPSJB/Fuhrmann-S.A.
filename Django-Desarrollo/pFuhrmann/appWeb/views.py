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

def nuevaCompra(request):
    if request.method == 'POST':
        formulario = compraForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/compra')
    else:
        formulario = compraForm()
    return render_to_response('compraForm.html', {'formulario':formulario}, context_instance=RequestContext(request))


def nuevaVenta(request):
    if request.method == 'POST':
        formulario = ventaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/venta')
    else:
        formulario = ventaForm()
    return render_to_response('ventaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def nuevaOrdenProduccion(request):
    if request.method == 'POST':
        formulario = nuevaOrdenProduccionForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/nuevaOrdenProduccion')
    else:
        formulario = nuevaOrdenProduccionForm()
    return render_to_response('nuevaOrdenProduccionForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarOrdenProduccion(request):
    orden = OrdenProduccion.objects.all()
    return render_to_response('modificarOrdenProduccion.html', {'lista':orden}, context_instance=RequestContext(request))
    
def modificarOrdenProduccionF(request):
    if request.method == 'POST':
        formulario = modificarOrdenProduccionForm(request.POST, request.FILES)
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
    
def registrarLote(request):
    if request.method == 'POST':
        formulario = LoteForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/index')
    else:
        formulario = LoteForm()
    return render_to_response('registrarLoteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarLote(request):
    lote = Lote.objects.all()
    return render_to_response('modificarLote.html', {'lista':lote}, context_instance=RequestContext(request))

def modificarLoteF(request, pk):
    lote = Lote.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = LoteForm(request.POST, request.FILES, instance=lote)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/index')
    else:
        formulario = LoteForm(instance = lote)
    return render_to_response('registrarLoteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    

def eliminarLote(request):
    lote = Lote.objects.all()   
    return render_to_response('eliminarLoteForm.html', {'lista':lote}, context_instance=RequestContext(request))

def eliminarLoteId(request, pk):
    lote = Lote.objects.get(pk=pk)
    lote.delete()
    lote = Lote.objects.all()
    return render_to_response('eliminarLoteForm.html', {'lista':lote}, context_instance=RequestContext(request))    

def registrarFardo(request):
    if request.method == 'POST':
        formulario = registrarFardoForm(request.POST, request.FILES)
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
        formulario = modificarFardoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarFardoF')
    else:
        formulario = modificarFardoForm()
    return render_to_response('modificarFardoForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    

def registrarEstancia(request):
    if request.method == 'POST':
        formulario = registrarEstanciaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarEstancia')
    else:
        formulario = registrarEstanciaForm()
    return render_to_response('registrarEstanciaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarEstancia(request):
    estancia = Estancia.objects.all()
    return render_to_response('modificarEstancia.html', {'lista':estancia}, context_instance=RequestContext(request))
    
def modificarEstanciaF(request):
    if request.method == 'POST':
        formulario = modificarEstanciaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarEstanciaF')
    else:
        formulario = modificarEstanciaForm()
    return render_to_response('modificarEstanciaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    
def eliminarEstancia(request):
    estancia = Estancia.objects.all()
    return render_to_response('eliminarEstanciaForm.html', {'lista':estancia}, context_instance=RequestContext(request))
    
def registrarProductor(request):
    if request.method == 'POST':
        formulario = registrarProductorForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarProductor')
    else:
        formulario = registrarProductorForm()
    return render_to_response('registrarProductorForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarProductor(request):
    productores = Productor.objects.all()
    return render_to_response('modificarProductor.html', {'lista':productores}, context_instance=RequestContext(request))
    
def modificarProductorF(request):
    if request.method == 'POST':
        formulario = modificarProductorForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarProductorF')
    else:
        formulario = modificarProductorForm()
    return render_to_response('modificarProductorForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    
def eliminarProductor(request):
    productores = Productor.objects.all()
    return render_to_response('eliminarProductorForm.html', {'lista':productores}, context_instance=RequestContext(request))
    

def registrarRepresentante(request):
    if request.method == 'POST':
        formulario = registrarRepresentanteForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarRepresentante')
    else:
        formulario = registrarRepresentanteForm()
    return render_to_response('registrarRepresentanteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarRepresentante(request):
    representantes = Representante.objects.all()
    return render_to_response('modificarRepresentante.html', {'lista':representantes}, context_instance=RequestContext(request))
    
def modificarRepresentanteF(request):
    if request.method == 'POST':
        formulario = modificarRepresentanteForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarRepresentanteF')
    else:
        formulario = modificarRepresentanteForm()
    return render_to_response('modificarRepresentanteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    
def eliminarRepresentante(request):
    representantes = Representante.objects.all()
    return render_to_response('eliminarRepresentanteForm.html', {'lista':representantes}, context_instance=RequestContext(request))
    
def registrarMaquinaria(request):
    if request.method == 'POST':
        formulario = registrarMaquinariaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/registrarMaquinaria')
    else:
        formulario = registrarMaquinariaForm()
    return render_to_response('registrarMaquinariaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarMaquinaria(request):
    maquinaria = Maquinaria.objects.all()
    return render_to_response('modificarMaquinaria.html', {'lista':maquinaria}, context_instance=RequestContext(request))
    
def modificarMaquinariaF(request):
    if request.method == 'POST':
        formulario = modificarMaquinariaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/modificarMaquinariaF')
    else:
        formulario = modificarMaquinariaForm()
    return render_to_response('modificarMaquinariaForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
    
def eliminarMaquinaria(request):
    maquinaria = Maquinaria.objects.all()
    return render_to_response('eliminarMaquinariaForm.html', {'lista':maquinaria}, context_instance=RequestContext(request))
    


