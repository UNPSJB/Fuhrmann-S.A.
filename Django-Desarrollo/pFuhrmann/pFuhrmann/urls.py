from django.conf.urls import patterns, include, url
from django.contrib import admin
from appWeb import views
from django.contrib.auth.views import login, logout

admin.autodiscover()
urlpatterns = patterns('',
    
    # ------ Estadisticas  
    url(r'^eRh/$', 'appWeb.views.estadisticasRepresentantes'),
    url(r'^eRl/$', 'appWeb.views.line'),
    
    url(r'^esta/$', 'appWeb.views.estadisticasMaq'),
    url(r'^esta/(?P<FI>.*)/(?P<FF>.*)/$', 'appWeb.views.estadisticasMaquinarias'),

    # ------ Adm. Login  
    url(r'^login/$', 'appWeb.views.login_user'),
    url(r'^logout/$', 'appWeb.views.logout'),
    url(r'^recoveryPassword/$', 'appWeb.views.recoveryPassword'),
    url(r'^recoveryPassword/(.*)/$', 'appWeb.views.recoveryPassword'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^acercaDe/', 'appWeb.views.acercaDe'),
    url(r'^$','appWeb.views.index'),
    url(r'^index/','appWeb.views.index'),
    url(r'^error_message/','appWeb.views.error_message'),
    url(r'^error_message_404/','appWeb.views.error_message_404'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # ------ Adm. Excel
    url(r'^excelRepresentantes/$', 'appWeb.views.excelRepresentantes'),        
    url(r'^excelProductores/$', 'appWeb.views.excelProductores'),        
    url(r'^excelLotes/$', 'appWeb.views.excelLotes'),        
    url(r'^excelFardos/$', 'appWeb.views.excelFardos'),        

    # ------ Adm. Compra
    url(r'^registrarCompra/$', 'appWeb.views.registrarCompra'),
    url(r'^listadoCompra/$', 'appWeb.views.listadoCompra'),
    url(r'^buscarCompra/(.*)/$', 'appWeb.views.buscarCompra'),
   
    # ------ Adm. Venta
    url(r'^registrarVenta/$', 'appWeb.views.registrarVenta'),
    url(r'^listadoVenta/$', 'appWeb.views.listadoVenta'),
    url(r'^buscarVenta/(.*)/$', 'appWeb.views.buscarVenta'),

    # ------ Adm. PDF
    url(r'^pdfEstancias/$', 'appWeb.views.pdfEstancias'),
    url(r'^pdfCompras/$', 'appWeb.views.pdfCompras'),
    url(r'^pdfVentas/$', 'appWeb.views.pdfVentas'),
    url(r'^pdfRepresentantes/$', 'appWeb.views.pdfRepresentantes'),
    url(r'^pdfProductores/$', 'appWeb.views.pdfProductores'),
    url(r'^pdfOp/$', 'appWeb.views.pdfOp'),

    # ------ Adm. Orden de produccion
    url(r'^registrarOrdenProduccion/$', 'appWeb.views.registrarOrdenProduccion'),
    url(r'^modificarOrdenProduccion/(\d+)/$', 'appWeb.views.modificarOrdenProduccion'),
    url(r'^cancelarOrdenProduccion/(\d+)/$', 'appWeb.views.cancelarOrdenProduccion'),
    url(r'^enviarFaseProduccion/$', 'appWeb.views.enviarFaseProduccion'),
    url(r'^verOrdenProduccion/(\d+)/$', 'appWeb.views.verOrdenProduccion'),
    url(r'^finalizarFaseProduccion/$', 'appWeb.views.finalizarFaseProduccion'),
    url(r'^listadoOrden/$', 'appWeb.views.listadoOrden'),
    url(r'^agregarDetalle/(\d+)/$', 'appWeb.views.mostrarEstancia'),
    url(r'^loteEstancia/(?P<estancia>.*)/(?P<orden>\d+)/$', 'appWeb.views.mostrarLotes'),
    url(r'^fardosLote/(\d+)/$', 'appWeb.views.mostrarFardos'),
    url(r'^agregaDetalleOrden/(?P<campos>.*)/(?P<orden>\d+)/$', 'appWeb.views.agregarDetalle'),
    url(r'^buscarOrden/(.*)/$', 'appWeb.views.buscarOrden'),
    url(r'^commitLoteVenta/(?P<cuadricula>.*)/(?P<orden>\d+)/$', 'appWeb.views.commitLoteVenta'),
    url(r'^agregarLoteVenta/(\d+)/$', 'appWeb.views.agregarLoteVenta'),
    url(r'^commitIniciarFase/(?P<orden>\d+)/(?P<nroSerie>\d+)/$', 'appWeb.views.commitIniciarFase'),
    url(r'^enviarFaseProduccion/(\d+)/$', 'appWeb.views.enviarFaseProduccion'),
    url(r'^finalizarFaseProduccion/(\d+)/$', 'appWeb.views.finalizarFaseProduccion'),

    # ------ Adm. Lotes
    url(r'^registrarLote/$', 'appWeb.views.registrarLote'),
    url(r'^listadoLotes/$', 'appWeb.views.listadoLotes'),
    #url(r'^modificarLote/(\d+)/$', 'appWeb.views.modificarLote'),
    url(r'^eliminarLote/(\d+)/$', 'appWeb.views.eliminarLoteId'),
    url(r'^buscarLote/(.*)/$', 'appWeb.views.buscarLote'),
    
    # ------ Adm. Fardos
    url(r'^registrarFardo/$', 'appWeb.views.registrarFardo'),
    url(r'^listadoFardos/$', 'appWeb.views.listadoFardos'),
    #url(r'^modificarFardo/(\d+)/$', 'appWeb.views.modificarFardo'),
    url(r'^buscarFardo/(.*)/$', 'appWeb.views.buscarFardo'),

    # ------ Adm. Estancias
    url(r'^listadoEstancias/$', 'appWeb.views.listadoEstancias'),
    url(r'^registrarEstancia/$', 'appWeb.views.registrarEstancia'),
    url(r'^modificarEstancia/([\d-]+)/$', 'appWeb.views.modificarEstancia'),
    url(r'^eliminarEstancia/([\d-]+)/$', 'appWeb.views.eliminarEstancia'),
    url(r'^buscarEstancia/(.*)/$', 'appWeb.views.buscarEstancia'),
    
    # ------ Adm. Productor
    url(r'^listadoProductores/$', 'appWeb.views.listadoProductores'),
    url(r'^registrarProductor/$', 'appWeb.views.registrarProductor'),
    url(r'^modificarProductor/([\d-]+)/$', 'appWeb.views.modificarProductor'),
    url(r'^eliminarProductor/([\d-]+)/$', 'appWeb.views.eliminarProductor'),
    url(r'^buscarProductor/(.*)/$', 'appWeb.views.buscarProductor'),

    # ------ Adm. Representante
    url(r'^listadoRepresentante/$', 'appWeb.views.listadoRepresentante'),
    url(r'^registrarRepresentante/$', 'appWeb.views.registrarRepresentante'),
    url(r'^modificarRepresentante/([\d-]+)/$', 'appWeb.views.modificarRepresentante'),
    url(r'^eliminarRepresentante/([\d-]+)/$', 'appWeb.views.eliminarRepresentante'),
    url(r'^buscarRepresentante/(.*)/$', 'appWeb.views.buscarRepresentante'),
    
    # ------ Adm. Maquinaria
    url(r'^listadoMaquinaria/$', 'appWeb.views.listadoMaquinaria'),
    url(r'^registrarMaquinaria/$', 'appWeb.views.registrarMaquinaria'),
    url(r'^modificarMaquinaria/(\d+)$', 'appWeb.views.modificarMaquinaria'),
    url(r'^eliminarMaquinaria/(\d+)/$', 'appWeb.views.eliminarMaquinaria'),
    url(r'^buscarMaquinaria/(.*)/$', 'appWeb.views.buscarMaquinaria'),
)