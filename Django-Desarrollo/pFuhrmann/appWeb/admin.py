from django.contrib import admin
from appWeb.models import *

class RepresentanteAdmin(admin.ModelAdmin):
	search_fields = ( 'DNI', 'Nombre', 'Apellido')

admin.site.register(Config)
admin.site.register(Productor)
admin.site.register(Representante, RepresentanteAdmin)
admin.site.register(Estancia)
admin.site.register(Lote)
admin.site.register(Fardo)
admin.site.register(TipoFardo)
admin.site.register(CompraLote)
admin.site.register(OrdenProduccion)
admin.site.register(Produccion)
admin.site.register(DetalleOrden)
admin.site.register(Servicio)
admin.site.register(LoteVenta)
admin.site.register(Venta)
admin.site.register(Maquinaria)

