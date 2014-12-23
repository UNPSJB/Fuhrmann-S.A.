# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompraLote'
        db.create_table(u'appWeb_compralote', (
            ('NroCompra', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Representante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Representante'])),
            ('Estancia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Estancia'])),
            ('FechaLlegada', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'appWeb', ['CompraLote'])

        # Adding model 'Venta'
        db.create_table(u'appWeb_venta', (
            ('NroVenta', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('LoteVenta', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appWeb.LoteVenta'], unique=True)),
            ('Cliente', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('FechaVenta', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'appWeb', ['Venta'])

        # Adding model 'Persona'
        db.create_table(u'appWeb_persona', (
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('DNI', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('Telefono', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('Baja', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'appWeb', ['Persona'])

        # Adding model 'Productor'
        db.create_table(u'appWeb_productor', (
            (u'persona_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appWeb.Persona'], unique=True)),
            ('CUIL', self.gf('django.db.models.fields.CharField')(max_length=13, primary_key=True)),
        ))
        db.send_create_signal(u'appWeb', ['Productor'])

        # Adding model 'Representante'
        db.create_table(u'appWeb_representante', (
            (u'persona_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appWeb.Persona'], unique=True)),
            ('NroLegajo', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=50, primary_key=True)),
            ('Zona', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'appWeb', ['Representante'])

        # Adding model 'Estancia'
        db.create_table(u'appWeb_estancia', (
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('CUIT', self.gf('django.db.models.fields.CharField')(max_length=13, primary_key=True)),
            ('Provincia', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Zona', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Baja', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Representante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Representante'])),
            ('Productor', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appWeb.Productor'], unique=True)),
        ))
        db.send_create_signal(u'appWeb', ['Estancia'])

        # Adding model 'Lote'
        db.create_table(u'appWeb_lote', (
            ('NroLote', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('TipoFardo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.TipoFardo'])),
            ('CantFardos', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=50)),
            ('Peso', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=50)),
            ('Baja', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Compra', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appWeb.CompraLote'], unique=True)),
            ('Estancia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Estancia'])),
            ('Cuadricula', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'appWeb', ['Lote'])

        # Adding model 'Fardo'
        db.create_table(u'appWeb_fardo', (
            ('NroFardo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Lote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Lote'])),
            ('Peso', self.gf('django.db.models.fields.FloatField')()),
            ('Rinde', self.gf('django.db.models.fields.FloatField')()),
            ('Finura', self.gf('django.db.models.fields.FloatField')()),
            ('CV', self.gf('django.db.models.fields.FloatField')()),
            ('AlturaMedia', self.gf('django.db.models.fields.FloatField')()),
            ('Romana', self.gf('django.db.models.fields.FloatField')()),
            ('DetalleOrden', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.DetalleOrden'], null=True, blank=True)),
        ))
        db.send_create_signal(u'appWeb', ['Fardo'])

        # Adding model 'TipoFardo'
        db.create_table(u'appWeb_tipofardo', (
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('Descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Baja', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'appWeb', ['TipoFardo'])

        # Adding model 'OrdenProduccion'
        db.create_table(u'appWeb_ordenproduccion', (
            ('NroOrden', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('FechaEmision', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('CantRequerida', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=50)),
            ('CV', self.gf('django.db.models.fields.FloatField')()),
            ('AlturaMedia', self.gf('django.db.models.fields.FloatField')()),
            ('Finura', self.gf('django.db.models.fields.FloatField')()),
            ('Romana', self.gf('django.db.models.fields.FloatField')()),
            ('Rinde', self.gf('django.db.models.fields.FloatField')()),
            ('Finalizada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Cancelada', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'appWeb', ['OrdenProduccion'])

        # Adding model 'DetalleOrden'
        db.create_table(u'appWeb_detalleorden', (
            ('NroDetalle', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('OrdenProduccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.OrdenProduccion'])),
        ))
        db.send_create_signal(u'appWeb', ['DetalleOrden'])

        # Adding model 'Servicio'
        db.create_table(u'appWeb_servicio', (
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('Descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ServicioPrevio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Servicio'], null=True, blank=True)),
            ('Transitorio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Baja', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'appWeb', ['Servicio'])

        # Adding model 'Produccion'
        db.create_table(u'appWeb_produccion', (
            ('NroProduccion', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Orden', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.OrdenProduccion'])),
            ('Servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Servicio'])),
            ('FechaInicio', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('FechaFin', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Maquinaria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Maquinaria'], null=True, blank=True)),
        ))
        db.send_create_signal(u'appWeb', ['Produccion'])

        # Adding model 'Maquinaria'
        db.create_table(u'appWeb_maquinaria', (
            ('NroSerie', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=50, primary_key=True)),
            ('Servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appWeb.Servicio'])),
            ('Descripcion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Baja', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'appWeb', ['Maquinaria'])

        # Adding model 'LoteVenta'
        db.create_table(u'appWeb_loteventa', (
            ('NroPartida', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Cantidad', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=50)),
            ('Cuadricula', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Baja', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('OrdenProduccion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appWeb.OrdenProduccion'], unique=True)),
        ))
        db.send_create_signal(u'appWeb', ['LoteVenta'])


    def backwards(self, orm):
        # Deleting model 'CompraLote'
        db.delete_table(u'appWeb_compralote')

        # Deleting model 'Venta'
        db.delete_table(u'appWeb_venta')

        # Deleting model 'Persona'
        db.delete_table(u'appWeb_persona')

        # Deleting model 'Productor'
        db.delete_table(u'appWeb_productor')

        # Deleting model 'Representante'
        db.delete_table(u'appWeb_representante')

        # Deleting model 'Estancia'
        db.delete_table(u'appWeb_estancia')

        # Deleting model 'Lote'
        db.delete_table(u'appWeb_lote')

        # Deleting model 'Fardo'
        db.delete_table(u'appWeb_fardo')

        # Deleting model 'TipoFardo'
        db.delete_table(u'appWeb_tipofardo')

        # Deleting model 'OrdenProduccion'
        db.delete_table(u'appWeb_ordenproduccion')

        # Deleting model 'DetalleOrden'
        db.delete_table(u'appWeb_detalleorden')

        # Deleting model 'Servicio'
        db.delete_table(u'appWeb_servicio')

        # Deleting model 'Produccion'
        db.delete_table(u'appWeb_produccion')

        # Deleting model 'Maquinaria'
        db.delete_table(u'appWeb_maquinaria')

        # Deleting model 'LoteVenta'
        db.delete_table(u'appWeb_loteventa')


    models = {
        u'appWeb.compralote': {
            'Estancia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Estancia']"}),
            'FechaLlegada': ('django.db.models.fields.DateField', [], {}),
            'Meta': {'ordering': "['NroCompra']", 'object_name': 'CompraLote'},
            'NroCompra': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Representante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appWeb.Representante']"})
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