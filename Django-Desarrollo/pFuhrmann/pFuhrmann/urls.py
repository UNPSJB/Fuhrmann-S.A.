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
 	url(r'^altaFardo/', 'appWeb.views.altaFardo'),
 	url(r'^modificarFardo/', 'appWeb.views.modificarFardo'), 	
 	url(r'^altaProductor/', 'appWeb.views.altaProductor'),
    url(r'^bajaProductor/', 'appWeb.views.bajaProductor'),
    url(r'^modificarProductor/', 'appWeb.views.modificarProductor'),
    url(r'^altaLote/', 'appWeb.views.altaLote'),
    url(r'^bajaLote/', 'appWeb.views.bajaLote'),
    url(r'^modificarLote/', 'appWeb.views.modificarLote'),
    url(r'^altaRepresentante/', 'appWeb.views.altaRepresentante'),
    url(r'^modificarRepresentante/', 'appWeb.views.modificarRepresentante'),
    url(r'^bajaRepresentante/', 'appWeb.views.bajaRepresentante'),
    url(r'^altaEstancia/', 'appWeb.views.altaEstancia'),
    url(r'^modificarEstancia/', 'appWeb.views.modificarEstancia'),
    url(r'^bajaEstancia/', 'appWeb.views.bajaEstancia'),
)