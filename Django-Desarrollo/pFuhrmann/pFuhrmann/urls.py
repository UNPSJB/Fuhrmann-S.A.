from django.conf.urls import patterns, include, url
from django.contrib import admin
from appWeb import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^index/','appWeb.views.index'),
    url(r'^$','appWeb.views.index'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #Registrar Operacion
    url(r'^registrarCompra/$', 'appWeb.views.registrarCompra'),
    url(r'^listadoCompra/$', 'appWeb.views.listadoCompra'),
    url(r'^registrarVenta/$', 'appWeb.views.registrarVenta'),
    url(r'^listadoVenta/$', 'appWeb.views.listadoVenta'),

    #Orden de produccion
    url(r'^registrarOrdenProduccion/$', 'appWeb.views.registrarOrdenProduccion'),
    url(r'^modificarOrdenProduccion/$', 'appWeb.views.modificarOrdenProduccion'),
    url(r'^cancelarOrdenProduccion/$', 'appWeb.views.cancelarOrdenProduccion'),
    url(r'^enviarFaseProduccion/$', 'appWeb.views.enviarFaseProduccion'),
    url(r'^finalizarFaseProduccion/$', 'appWeb.views.finalizarFaseProduccion'),
    url(r'^listadoOrden/$', 'appWeb.views.listadoOrden'),
    
    #Lotes y Fardos
    url(r'^registrarLote/$', 'appWeb.views.registrarLote'),
    url(r'^listadoLotes/$', 'appWeb.views.listadoLotes'),
    url(r'^modificarLote/(\d+)/$', 'appWeb.views.registrarLote'),
    url(r'^eliminarLote/(\d+)/$', 'appWeb.views.eliminarLoteId'),

    url(r'^registrarFardo/$', 'appWeb.views.registrarFardo'),
    url(r'^listadoFardos/$', 'appWeb.views.listadoFardos'),
    url(r'^modificarFardo/(\d+)/$', 'appWeb.views.registrarFardo'),

    # ------ Adm. Estancias
    url(r'^listadoEstancias/$', 'appWeb.views.listadoEstancias'),
    url(r'^modificarEstancia/$', 'appWeb.views.modificarEstancia'),
    url(r'^modificarEstancia/([\d-]+)/$', 'appWeb.views.modificarEstancia'),
    url(r'^eliminarEstancia/([\d-]+)/$', 'appWeb.views.eliminarEstancia'),
    
    # ------ Adm. Productor
    url(r'^listadoProductores/$', 'appWeb.views.listadoProductores'),
    url(r'^modificarProductor/$', 'appWeb.views.modificarProductor'),
    url(r'^modificarProductor/([\d-]+)/$', 'appWeb.views.modificarProductor'),
    url(r'^eliminarProductor/([\d-]+)/$', 'appWeb.views.eliminarProductor'),
    

    # ------ Adm. Representante
    url(r'^listadoRepresentante/$', 'appWeb.views.listadoRepresentante'),
    url(r'^modificarRepresentante/$', 'appWeb.views.modificarRepresentante'),
    url(r'^modificarRepresentante/(\d+)$', 'appWeb.views.modificarRepresentante'),
    url(r'^eliminarRepresentante/(\d+)/$', 'appWeb.views.eliminarRepresentante'),
    

    ## ------ Adm. Maquinaria
    url(r'^listadoMaquinaria/$', 'appWeb.views.listadoMaquinaria'),
    url(r'^registrarMaquinaria/$', 'appWeb.views.registrarMaquinaria'),
    url(r'^eliminarMaquinaria/(\d+)/$', 'appWeb.views.eliminarMaquinaria'),
    

    #Url's Dinamicas
    url(r'^eliminarLote/(?P<pk>\d+)/$', 'appWeb.views.eliminarLoteId'),
)
