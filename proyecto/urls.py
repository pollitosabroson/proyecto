from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','contend.views.ingresar'),
	url(r'^inicio/$','contend.views.inicio'),
	url(r'^inicio/citas/$','contend.views.new_pacient'),
	url(r'^consulta/$','contend.views.consulta'),
	#url(r'^esta/$','contend.views.estadisticas'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ingresar/$','contend.views.ingresar'),
    url(r'^usuarios/$','contend.views.datos'),
    url(r'^cerrar/$', 'contend.views.cerrar'),
    #url(r'^media/(?P<path>.*)$','django.views.static.serve',
	#	{'document_root':settings.MEDIA_ROOT,},
)