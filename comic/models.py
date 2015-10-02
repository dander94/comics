from django.db import models

# Create your models here.

class Location(models.Model):
	nombre=models.CharField(max_length=40)
	def __str__(self):
		return self.nombre

class Collection(models.Model):
	nombre=models.CharField(max_length=100,blank=False,null=False)
	numeros_totales=models.IntegerField(default=0)
	def __str__(self):
		return self.nombre
class Comic(models.Model):
	coleccion=models.ForeignKey(Collection)
	nombre=models.CharField(max_length=100)
	numero_en_coleccion=models.IntegerField(default=0)
	localizacion = models.ForeignKey(Location)
	def __str__(self):
		return self.nombre
