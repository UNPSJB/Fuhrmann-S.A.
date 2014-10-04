from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
	url(r'^index/','appWeb.views.index'),
	url(r'^$','appWeb.views.index'),
	
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    """Registrar Operacion"""
    url(r'^compra/$', 'appWeb.views.nuevaCompra'),
 	url(r'^venta/$', 'appWeb.views.nuevaVenta'),

    """Orden de produccion"""
    url(r'^nuevaOrdenProduccion/$', 'appWeb.views.nuevaOrdenProduccion'),
    url(r'^modificarOrdenProduccion/$', 'appWeb.views.modificarOrdenProduccion'),
    url(r'^cancelarOrdenProduccion/$', 'appWeb.views.cancelarOrdenProduccion'),
    url(r'^enviarFaseProduccion/$', 'appWeb.views.enviarFaseProduccion'),
    url(r'^finalizarFaseProduccion/$', 'appWeb.views.finalizarFaseProduccion'),
    
    """Lotes y Fardos"""
    url(r'^registrarLote/$', 'appWeb.views.registrarLote'),
    url(r'^modificarLote/$', 'appWeb.views.modificarLote'),
    url(r'^borrarLote/$', 'appWeb.views.borrarLote'),
    url(r'^registrarFardo/$', 'appWeb.views.registrarFardo'),
    url(r'^modificarFardo/$', 'appWeb.views.modificarFardo'),

    """Adm. Estancias"""
    url(r'^registrarEstancia/$', 'appWeb.views.registrarEstancia'),
    url(r'^modificarEstancia/$', 'appWeb.views.modificarEstancia'),
    url(r'^borrarEstancia/$', 'appWeb.views.borrarEstancia'),

    """Adm. Personas"""
    url(r'^registrarProductor/$', 'appWeb.views.registrarProductor'),
    url(r'^modificarProductor/$', 'appWeb.views.modificarProductor'),
    url(r'^borrarProductor/$', 'appWeb.views.borrarProductor'),
    url(r'^registrarRepresentante/$', 'appWeb.views.registrarRepresentante'),
    url(r'^modificarRepresentante/$', 'appWeb.views.modificarRepresentante'),
    url(r'^borrarRepresentante/$', 'appWeb.views.borrarRepresentante'),

    """Adm. Maquinaria"""
    url(r'^registrarMaquinaria/$', 'appWeb.views.registrarMaquinaria'),
    url(r'^modificarMaquinaria/$', 'appWeb.views.modificarMaquinaria'),
    url(r'^borrarMaquinaria/$', 'appWeb.views.borrarMaquinaria'),

    #Url's de Forms para modificar Datos
    url(r'^modificarOrdenProduccionF/$', 'appWeb.views.modificarOrdenProduccionF'),
    url(r'^modificarLoteF/$', 'appWeb.views.modificarLoteF'),
    url(r'^modificarFardoF/$', 'appWeb.views.modificarFardoF'),
    url(r'^modificarEstanciaF/$', 'appWeb.views.modificarEstanciaF'),
    url(r'^modificarProductorF/$', 'appWeb.views.modificarProductorF'),
    url(r'^modificarRepresentanteF/$', 'appWeb.views.modificarRepresentanteF'),
    url(r'^modificarMaquinariaF/$', 'appWeb.views.modificarMaquinariaF'),
)
