from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index (request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def altaproductor (request):
	return render_to_response('altaproductor.html', context_instance=RequestContext(request))

def bajaproductor (request):
	return render_to_response('bajaproductor.html', context_instance=RequestContext(request))

def modificarproductor (request):
	return render_to_response('modificarproductor.html', context_instance=RequestContext(request))

def altalote (request):
	return render_to_response('altalote.html', context_instance=RequestContext(request))

def bajalote (request):
	return render_to_response('bajalote.html', context_instance=RequestContext(request))

def modificarlote (request):
	return render_to_response('modificarlote.html', context_instance=RequestContext(request))
