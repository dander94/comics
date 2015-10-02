from django.shortcuts import render

# Create your views here.

from .models import Location, Collection, Comic
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
	print("IND")
	return render(request,'comic/index.html')
	

def crear(request):
	
	try:
		nombre_nv = request.POST['nombre']
		print(nombre_nv)
	except (KeyError, Location.DoesNotExist):
		return render(request,'comic/index.html');
	else:
		localizacion=Location()
		localizacion.nombre=nombre_nv
		localizacion.save()
		return HttpResponseRedirect(reverse('comics:location',args=()));	

class LocationView(generic.ListView):
	template_name ='comic/location.html'
	context_object_name = 'location_list'
	def get_queryset(self):
		return Location.objects.order_by('nombre')

	
