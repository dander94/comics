from rest_framework import serializers
from .models import Comic
class ComicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comic
		fields = ('id','nombre','numero_en_coleccion','localizacion','coleccion')
