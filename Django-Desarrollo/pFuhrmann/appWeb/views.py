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
