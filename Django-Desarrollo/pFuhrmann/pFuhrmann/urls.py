from django.conf.urls import patterns, include, url
from django.contrib import admin
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
    url(r'^nuevaOrdenProduccion/$', 'appWeb.views.nuevaOrdenProduccion'),
    url(r'^modificarOrdenProduccion/$', 'appWeb.views.modificarOrdenProduccion'),
    url(r'^cancelarOrdenProduccion/$', 'appWeb.views.cancelarOrdenProduccion'),
    url(r'^enviarFaseProduccion/$', 'appWeb.views.enviarFaseProduccion'),
    url(r'^finalizarFaseProduccion/$', 'appWeb.views.finalizarFaseProduccion'),
    url(r'^listadoOrden/$', 'appWeb.views.listadoOrden'),
    
    #Lotes y Fardos
    url(r'^registrarLote/$', 'appWeb.views.registrarLote'),
    url(r'^listadoLotes/$', 'appWeb.views.listadoLotes'),
    url(r'^modificarLote/$', 'appWeb.views.modificarLote'),
    url(r'^modificarLote/(\d+)/$', 'appWeb.views.modificarLoteF'),
    url(r'^eliminarLote/(\d+)/$', 'appWeb.views.eliminarLoteId'),

    url(r'^registrarFardo/$', 'appWeb.views.registrarFardo'),
    url(r'^listadoFardos/$', 'appWeb.views.listadoFardos'),
    url(r'^modificarFardo/$', 'appWeb.views.modificarFardo'),

    #Adm. Estancias
    url(r'^registrarEstancia/$', 'appWeb.views.registrarEstancia'),
    url(r'^listadoEstancias/$', 'appWeb.views.listadoEstancias'),
    url(r'^modificarEstancia/$', 'appWeb.views.modificarEstancia'),
    url(r'^modificarEstancia/(\d+)$', 'appWeb.views.modificarEstanciaF'),
    url(r'^eliminarEstancia/(\d+)$', 'appWeb.views.eliminarEstanciaId'),

    #Adm. Personas
    url(r'^registrarProductor/$', 'appWeb.views.registrarProductor'),
    url(r'^listadoProductores/$', 'appWeb.views.listadoProductores'),
    url(r'^modificarProductor/$', 'appWeb.views.modificarProductor'),
    url(r'^eliminarProductor/$', 'appWeb.views.eliminarProductor'),
    url(r'^registrarRepresentante/$', 'appWeb.views.registrarRepresentante'),
    url(r'^modificarRepresentante/$', 'appWeb.views.modificarRepresentante'),
    url(r'^eliminarRepresentante/$', 'appWeb.views.eliminarRepresentante'),

    #Adm. Maquinaria
    url(r'^registrarMaquinaria/$', 'appWeb.views.registrarMaquinaria'),
    url(r'^modificarMaquinaria/$', 'appWeb.views.modificarMaquinaria'),
    url(r'^modificarMaquinaria/(\d+)$', 'appWeb.views.modificarMaquinariaF'),
    url(r'^eliminarMaquinaria/(\d+)$', 'appWeb.views.eliminarMaquinariaId'),
    url(r'^listadoMaquinaria/$', 'appWeb.views.listadoMaquinaria'),

    #Url's de Forms para modificar Datos
    url(r'^modificarOrdenProduccionF/$', 'appWeb.views.modificarOrdenProduccionF'),
    url(r'^modificarLoteF/$', 'appWeb.views.modificarLoteF'),
    url(r'^modificarFardoF/$', 'appWeb.views.modificarFardoF'),
    url(r'^modificarEstanciaF/$', 'appWeb.views.modificarEstanciaF'),
    url(r'^modificarProductorF/$', 'appWeb.views.modificarProductorF'),
    url(r'^modificarRepresentanteF/$', 'appWeb.views.modificarRepresentanteF'),
    url(r'^modificarMaquinariaF/$', 'appWeb.views.modificarMaquinariaF'),

    #Url's Dinamicas
    url(r'^eliminarLote/(?P<pk>\d+)/$', 'appWeb.views.eliminarLoteId'),
    url(r'^eliminarEstancia/(?P<pk>\d+)/$', 'appWeb.views.eliminarEstanciaId'),
    url(r'^eliminarMaquinaria/(?P<pk>\d+)/$', 'appWeb.views.eliminarMaquinariaId'),
)
