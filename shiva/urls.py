from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'subscription.views.index', name='subscription'),
    url(r'^mtt/', include('mtt.urls')),
]
