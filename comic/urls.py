from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name="index"),
		url(r'^location/$', views.LocationView.as_view(),name='location'),
		url(r'^collection/$', views.CollectionView.as_view(),name='collection'),
url(r'^location/create/$', views.crear_localizacion,name='create_loc'),
url(r'^collection/create/$', views.crear_coleccion,name='create_col')
]
