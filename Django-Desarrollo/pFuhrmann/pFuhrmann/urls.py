from django.conf.urls import patterns, include, url
from django.contrib import admin
from appWeb import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^index/','appWeb.views.index'),
    url(r'^$','appWeb.views.index'),
    url(r'^usuario/$','appWeb.views.nuevo_usuario'),
    url(r'^ingresar/$','appWeb.views.ingresar'),
    url(r'^privado/$','appWeb.views.privado'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #Registrar Operacion
    url(r'^registrarCompra/$', 'appWeb.views.registrarCompra'),
    url(r'^listadoCompra/$', 'appWeb.views.listadoCompra'),
    url(r'^buscarCompra/(.*)/$', 'appWeb.views.buscarCompra'),

    url(r'^registrarVenta/$', 'appWeb.views.registrarVenta'),
    url(r'^listadoVenta/$', 'appWeb.views.listadoVenta'),
    url(r'^buscarVenta/(.*)/$', 'appWeb.views.buscarVenta'),

    #Orden de produccion
    url(r'^registrarOrdenProduccion/$', 'appWeb.views.registrarOrdenProduccion'),
    url(r'^modificarOrdenProduccion/(\d+)/$', 'appWeb.views.registrarOrdenProduccion'),
    url(r'^cancelarOrdenProduccion/(\d+)/$', 'appWeb.views.cancelarOrdenProduccion'),
    url(r'^enviarFaseProduccion/$', 'appWeb.views.enviarFaseProduccion'),
    url(r'^verOrdenProduccion/(\d+)/$', 'appWeb.views.verOrdenProduccion'),
    url(r'^finalizarFaseProduccion/$', 'appWeb.views.finalizarFaseProduccion'),
    url(r'^listadoOrden/$', 'appWeb.views.listadoOrden'),
    url(r'^agregarDetalle/(\d+)/$', 'appWeb.views.mostrarEstancia'),

    url(r'^loteEstancia/([\d-]+)/$', 'appWeb.views.mostrarLotes'),
    url(r'^fardosLote/(\d+)/$', 'appWeb.views.mostrarFardos'),
    url(r'^agregaDetalleOrden/(?P<campos>.*)/(?P<orden>\d+)/$', 'appWeb.views.agregarDetalle'),
    url(r'^buscarOrden/(.*)/$', 'appWeb.views.buscarOrden'),

    

    url(r'^commitLoteVenta/(?P<cuadricula>.*)/(?P<orden>\d+)/$', 'appWeb.views.commitLoteVenta'),
    url(r'^agregarLoteVenta/(\d+)/$', 'appWeb.views.agregarLoteVenta'),





    #Lotes y Fardos
    url(r'^registrarLote/$', 'appWeb.views.registrarLote'),
    url(r'^listadoLotes/$', 'appWeb.views.listadoLotes'),
    url(r'^modificarLote/(\d+)/$', 'appWeb.views.registrarLote'),
    url(r'^eliminarLote/(\d+)/$', 'appWeb.views.eliminarLoteId'),
    url(r'^buscarLote/(.*)/$', 'appWeb.views.buscarLote'),

    url(r'^registrarFardo/$', 'appWeb.views.registrarFardo'),
    url(r'^listadoFardos/$', 'appWeb.views.listadoFardos'),
    url(r'^modificarFardo/(\d+)/$', 'appWeb.views.registrarFardo'),
    url(r'^buscarFardo/(.*)/$', 'appWeb.views.buscarFardo'),

    # ------ Adm. Estancias
    url(r'^listadoEstancias/$', 'appWeb.views.listadoEstancias'),
    url(r'^registrarEstancia/$', 'appWeb.views.registrarEstancia'),
    url(r'^modificarEstancia/([\d-]+)/$', 'appWeb.views.modificarEstancia'),
    url(r'^eliminarEstancia/([\d-]+)/$', 'appWeb.views.eliminarEstancia'),
    url(r'^buscarEstancia/(.*)/$', 'appWeb.views.buscarEstancia'),
    
    # ------ Adm. Productor
    url(r'^listadoProductores/$', 'appWeb.views.listadoProductores'),
    url(r'^modificarProductor/$', 'appWeb.views.modificarProductor'),
    url(r'^modificarProductor/([\d-]+)/$', 'appWeb.views.modificarProductor'),
    url(r'^eliminarProductor/([\d-]+)/$', 'appWeb.views.eliminarProductor'),
    url(r'^buscarProductor/(.*)/$', 'appWeb.views.buscarProductor'),


    # ------ Adm. Representante
    url(r'^listadoRepresentante/$', 'appWeb.views.listadoRepresentante'),
    url(r'^registrarRepresentante/$', 'appWeb.views.modificarRepresentante'),
    url(r'^modificarRepresentante/(\d+)$', 'appWeb.views.modificarRepresentante'),
    url(r'^eliminarRepresentante/(\d+)/$', 'appWeb.views.eliminarRepresentante'),
    url(r'^buscarRepresentante/(.*)/$', 'appWeb.views.buscarRepresentante'),
    

    ## ------ Adm. Maquinaria
    url(r'^listadoMaquinaria/$', 'appWeb.views.listadoMaquinaria'),
    url(r'^registrarMaquinaria/$', 'appWeb.views.registrarMaquinaria'),
    url(r'^modificarMaquinaria/(\d+)$', 'appWeb.views.modificarMaquinaria'),
    url(r'^eliminarMaquinaria/(\d+)/$', 'appWeb.views.eliminarMaquinaria'),
    url(r'^buscarMaquinaria/(.*)/$', 'appWeb.views.buscarMaquinaria'),



  #  url(r'^pdf/$', 'appWeb/MyPDF.as_view()'),


)
