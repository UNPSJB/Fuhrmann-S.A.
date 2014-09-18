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

<<<<<<< HEAD

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
		formulario = registrarLoteForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/registrarLote')
	else:
		formulario = registrarLoteForm()
	return render_to_response('registrarLoteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))

def modificarLote(request):
	lote = Lote.objects.all()
	return render_to_response('modificarLote.html', {'lista':lote}, context_instance=RequestContext(request))
	
def modificarLoteF(request):
	if request.method == 'POST':
		formulario = modificarLoteForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/modificarLoteF')
	else:
		formulario = modificarLoteForm()
	return render_to_response('modificarLoteForm.html', {'formulario':formulario}, context_instance=RequestContext(request))
	

def borrarLote(request):
	lote = Lote.objects.all()
	return render_to_response('borrarLoteForm.html', {'lista':lote}, context_instance=RequestContext(request))
	
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
		formulario = modificarLoteForm()
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
	
def borrarEstancia(request):
	estancia = Estancia.objects.all()
	return render_to_response('borrarEstanciaForm.html', {'lista':estancia}, context_instance=RequestContext(request))
	
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
	
def borrarProductor(request):
	productores = Productor.objects.all()
	return render_to_response('borrarProductorForm.html', {'lista':productores}, context_instance=RequestContext(request))
	

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
	
def borrarRepresentante(request):
	representantes = Representante.objects.all()
	return render_to_response('borrarRepresentanteForm.html', {'lista':representantes}, context_instance=RequestContext(request))
	


=======
def altaMaquinaria (request):
	return render_to_response('altaMaquinaria.html', context_instance=RequestContext(request))

def modificarMaquinaria (request):
	return render_to_response('modificarMaquinaria.html', context_instance=RequestContext(request))

def bajaMaquinaria (request):
	return render_to_response('bajaMaquinaria.html', context_instance=RequestContext(request))

def liberarMaquinaria (request):
	return render_to_response('liberarMaquinaria.html', context_instance=RequestContext(request))

def altaFardo (request):
	return render_to_response('altaFardo.html', context_instance=RequestContext(request))

def modificarFardo (request):
	return render_to_response('modificarFardo.html', context_instance=RequestContext(request))

def altaProductor (request):
	return render_to_response('altaProductor.html', context_instance=RequestContext(request))

def bajaProductor (request):
	return render_to_response('bajaProductor.html', context_instance=RequestContext(request))

def modificarProductor (request):
	return render_to_response('modificarProductor.html', context_instance=RequestContext(request))

def altaLote (request):
	return render_to_response('altaLote.html', context_instance=RequestContext(request))

def bajaLote (request):
	return render_to_response('bajaLote.html', context_instance=RequestContext(request))

def modificarLote (request):
	return render_to_response('modificarLote.html', context_instance=RequestContext(request))

def altaRepresentante (request):
	return render_to_response('altaRepresentante.html', context_instance=RequestContext(request))

def modificarRepresentante (request):
	return render_to_response('modificarRepresentante.html', context_instance=RequestContext(request))

def bajaRepresentante (request):
	return render_to_response('bajaRepresentante.html', context_instance=RequestContext(request))

def altaEstancia (request):
	return render_to_response('altaEstancia.html', context_instance=RequestContext(request))

def modificarEstancia (request):
	return render_to_response('modificarEstancia.html', context_instance=RequestContext(request))

def bajaEstancia (request):
	return render_to_response('bajaEstancia.html', context_instance=RequestContext(request))
>>>>>>> 387f0800cc9a414db1c072eaa9f464b36957e601
