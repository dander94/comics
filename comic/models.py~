from django.db import models

# Create your models here.

class Location(models.Model):
	nombre=models.CharField(max_length=40)

class Collection(models.Model):
	nombre=models.CharField(max_length=100)
	numeros_totales=models.IntegerField(default=0)
class Comic(models.Model):
	coleccion=models.ForeignKey(Collection)
	nombre=models.CharField(max_length=100)
	numero_en_coleccion=models.IntegerField(default=0)
	localizacion = models.ForeignKey(Location)
	
