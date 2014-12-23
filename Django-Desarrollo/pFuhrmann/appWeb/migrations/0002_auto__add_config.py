# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Config'
        db.create_table(u'appWeb_config', (
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'appWeb', ['Config'])


    def backwards(self, orm):
        # Deleting model 'Config'
        db.delete_table(u'appWeb_config')


    models = {
        u'appWeb.compralote': {
            'Estancia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Estancia']"}),
            'FechaLlegada': ('django.db.models.fields.DateField', [], {}),
            'Meta': {'ordering': "['NroCompra']", 'object_name': 'CompraLote'},
            'NroCompra': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Representante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Representante']"})
        },
        u'appWeb.config': {
            'Meta': {'object_name': 'Config'},
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'appWeb.detalleorden': {
            'Meta': {'ordering': "['NroDetalle']", 'object_name': 'DetalleOrden'},
            'NroDetalle': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'OrdenProduccion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.OrdenProduccion']"})
        },
        u'appWeb.estancia': {
            'Baja': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'CUIT': ('django.db.models.fields.CharField', [], {'max_length': '13', 'primary_key': 'True'}),
            'Meta': {'ordering': "['Nombre']", 'object_name': 'Estancia'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Productor': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['appWeb.Productor']", 'unique': 'True'}),
            'Provincia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Representante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Representante']"}),
            'Zona': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'appWeb.fardo': {
            'AlturaMedia': ('django.db.models.fields.FloatField', [], {}),
            'CV': ('django.db.models.fields.FloatField', [], {}),
            'DetalleOrden': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.DetalleOrden']", 'null': 'True', 'blank': 'True'}),
            'Finura': ('django.db.models.fields.FloatField', [], {}),
            'Lote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Lote']"}),
            'Meta': {'ordering': "['NroFardo']", 'object_name': 'Fardo'},
            'NroFardo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Peso': ('django.db.models.fields.FloatField', [], {}),
            'Rinde': ('django.db.models.fields.FloatField', [], {}),
            'Romana': ('django.db.models.fields.FloatField', [], {})
        },
        u'appWeb.lote': {
            'Baja': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'CantFardos': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '50'}),
            'Compra': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['appWeb.CompraLote']", 'unique': 'True'}),
            'Cuadricula': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Estancia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Estancia']"}),
            'Meta': {'ordering': "['NroLote']", 'object_name': 'Lote'},
            'NroLote': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Peso': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '50'}),
            'TipoFardo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.TipoFardo']"})
        },
        u'appWeb.loteventa': {
            'Baja': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Cantidad': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '50'}),
            'Cuadricula': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'ordering': "['NroPartida']", 'object_name': 'LoteVenta'},
            'NroPartida': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'OrdenProduccion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['appWeb.OrdenProduccion']", 'unique': 'True'})
        },
        u'appWeb.maquinaria': {
            'Baja': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['NroSerie']", 'object_name': 'Maquinaria'},
            'NroSerie': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '50', 'primary_key': 'True'}),
            'Servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Servicio']"})
        },
        u'appWeb.ordenproduccion': {
            'AlturaMedia': ('django.db.models.fields.FloatField', [], {}),
            'CV': ('django.db.models.fields.FloatField', [], {}),
            'Cancelada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'CantRequerida': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '50'}),
            'FechaEmision': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Finalizada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Finura': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'ordering': "['NroOrden']", 'object_name': 'OrdenProduccion'},
            'NroOrden': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Rinde': ('django.db.models.fields.FloatField', [], {}),
            'Romana': ('django.db.models.fields.FloatField', [], {}),
            'Servicio': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['appWeb.Servicio']", 'null': 'True', 'through': u"orm['appWeb.Produccion']", 'blank': 'True'})
        },
        u'appWeb.persona': {
            'Apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Baja': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'DNI': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['Apellido']", 'object_name': 'Persona'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Telefono': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'appWeb.produccion': {
            'FechaFin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'FechaInicio': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Maquinaria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Maquinaria']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['NroProduccion']", 'object_name': 'Produccion'},
            'NroProduccion': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Orden': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.OrdenProduccion']"}),
            'Servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Servicio']"})
        },
        u'appWeb.productor': {
            'CUIL': ('django.db.models.fields.CharField', [], {'max_length': '13', 'primary_key': 'True'}),
            'Meta': {'ordering': "['Apellido']", 'object_name': 'Productor', '_ormbases': [u'appWeb.Persona']},
            u'persona_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['appWeb.Persona']", 'unique': 'True'})
        },
        u'appWeb.representante': {
            'Meta': {'ordering': "['Apellido']", 'object_name': 'Representante', '_ormbases': [u'appWeb.Persona']},
            'NroLegajo': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '50', 'primary_key': 'True'}),
            'Zona': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'persona_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['appWeb.Persona']", 'unique': 'True'})
        },
        u'appWeb.servicio': {
            'Baja': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'Servicio'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'ServicioPrevio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Servicio']", 'null': 'True', 'blank': 'True'}),
            'Transitorio': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'appWeb.tipofardo': {
            'Baja': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'TipoFardo'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'appWeb.venta': {
            'Cliente': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'FechaVenta': ('django.db.models.fields.DateField', [], {}),
            'LoteVenta': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['appWeb.LoteVenta']", 'unique': 'True'}),
            'Meta': {'ordering': "['NroVenta']", 'object_name': 'Venta'},
            'NroVenta': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['appWeb']