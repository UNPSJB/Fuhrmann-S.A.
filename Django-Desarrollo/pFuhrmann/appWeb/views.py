from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index (request):
	return render_to_response('index.html', context_instance=RequestContext(request))
def altaMaquinaria (request):
	return render_to_response('altaMaquinaria.html', context_instance=RequestContext(request))
def modificarMaquinaria (request):
	return render_to_response('modificarMaquinaria.html', context_instance=RequestContext(request))
def bajaMaquinaria (request):
	return render_to_response('bajaMaquinaria.html', context_instance=RequestContext(request))
def liberarMaquinaria (request):
	return render_to_response('liberarMaquinaria.html', context_instance=RequestContext(request))
def altaClasificacionFardo (request):
	return render_to_response('altaClasificacionFardo.html', context_instance=RequestContext(request))
def modificacionFardo (request):
	return render_to_response('modificacionFardo.html', context_instance=RequestContext(request))
def altalote (request):
	return render_to_response('altalote.html', context_instance=RequestContext(request))