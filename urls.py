from django.urls import path

from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),
	
	# /music//712/
	path(r'^(?p<album_id[0-9]+)$', views.detail, name='detail' ),
	
		
]