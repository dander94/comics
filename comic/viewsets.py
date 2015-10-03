from .models import Comic
from .serializers import ComicSerializer
from rest_framework import viewsets

class ComicViewSet(viewsets.ModelViewSet):
	
	serializer_class = ComicSerializer
	queryset = Comic.objects.all()

