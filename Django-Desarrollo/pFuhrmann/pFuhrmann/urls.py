from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$','appWeb.views.index'),
    url(r'^admin/', include(admin.site.urls)),

 	url(r'^altaMaquinaria/', 'appWeb.views.altaMaquinaria'),
 	url(r'^modificarMaquinaria/', 'appWeb.views.modificarMaquinaria'),
 	url(r'^bajaMaquinaria/', 'appWeb.views.bajaMaquinaria'),
 	url(r'^liberarMaquinaria/', 'appWeb.views.liberarMaquinaria'),
 	url(r'^altaClasificacionFardo/', 'appWeb.views.altaClasificacionFardo'),
 	url(r'^modificacionFardo/', 'appWeb.views.modificacionFardo'),
   	url(r'^altalote/', 'appWeb.views.altalote'),
)
