from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'mtt.views.minutestotakeoff', name='mtt'),
    url(r'^maps$', 'mtt.views.maps', name='maps'),    
]
