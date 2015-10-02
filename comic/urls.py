from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name="index"),
		url(r'^location/$', views.LocationView.as_view(),name='location'),
url(r'^location/create/$', views.crear,name='create_loc')
]
