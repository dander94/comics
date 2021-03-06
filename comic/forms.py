from django import forms

from .models import Comic,Collection,Location

class CollectionForm(forms.ModelForm):
	class Meta:
		model = Collection
		fields = ('nombre','numeros_totales',)
class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = ('nombre',)
class ComicForm(forms.ModelForm):
	class Meta:
		model = Comic
		fields = ('nombre','numero_en_coleccion','localizacion',)
