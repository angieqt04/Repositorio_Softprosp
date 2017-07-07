from django.conf.urls import patterns,include, url
from django.contrib import admin

from core_apps.cuantitativas.Benchmarking import index

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^benchmarking/', include('core_apps.cuantitativas.Benchmarking.urls', namespace="benchmarking")),
                       )
