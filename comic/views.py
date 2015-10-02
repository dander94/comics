from django.shortcuts import render

# Create your views here.

from .models import Location, Collection, Comic
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import CollectionForm,LocationForm
from django.contrib import messages

def index(request):
	
	return render(request,'comic/index.html')
	

def crear_localizacion(request):
	
	try:
		form = LocationForm(request.POST)
		nombre_nv = request.POST['nombre']
	except (KeyError):
		return render(request,'comic/index.html');
	else:
		if form.is_valid():
			localizacion=Location()
			localizacion.nombre=nombre_nv
			localizacion.save()
		else:
			messages.add_message(request, messages.ERROR, 'Rellene el formulario correctamente')
		return HttpResponseRedirect(reverse('comics:location',args=()));

def crear_coleccion(request):
	try:	
		form = CollectionForm(request.POST)
		nombre_nv = request.POST['nombre']
		num_nv = request.POST['numeros_totales']
	except (KeyError):
		return render(request,'comic/index.html');
	else:
		if form.is_valid():
			coleccion=Collection()
			coleccion.nombre=nombre_nv
			coleccion.numeros_totales=num_nv
			coleccion.save()
		else:
			messages.add_message(request, messages.ERROR, 'Rellene el formulario correctamente')
		return HttpResponseRedirect(reverse('comics:collection',args=()))
		

class LocationView(generic.ListView):
	template_name ='comic/location.html'
	context_object_name = 'location_list'
	form = LocationForm();
	def get_queryset(self):
		return Location.objects.order_by('nombre')
	def get_context_data(self, *args, **kwargs):
		context = super(LocationView,self).get_context_data( *args, **kwargs)
		context['form']=self.form;
		return context

class CollectionView(generic.ListView):
	template_name ='comic/collection.html'
	context_object_name = 'collection_list'
	form = CollectionForm();
	def get_queryset(self):
		return Collection.objects.order_by('nombre')
	def get_context_data(self, *args, **kwargs):
		context = super(CollectionView,self).get_context_data( *args, **kwargs)
		context['form']=self.form;
		return context
	

	
