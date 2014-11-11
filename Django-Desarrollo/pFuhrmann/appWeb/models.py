from django.db import models

class CompraLote(models.Model):
    NroCompra = models.AutoField(primary_key = True)
    Representante = models.ForeignKey('Representante')
    Estancia = models.ForeignKey('Estancia', null = True)
    FechaLlegada = models.DateField()
    
    def __unicode__(self):
        return "%s" % (str(self.Estancia) + " - " + str(self.FechaLlegada))

class Venta(models.Model):
    NroVenta = models.AutoField(primary_key = True)
    LoteVenta = models.OneToOneField('LoteVenta')
    Cliente = models.CharField(max_length=50)
    FechaVenta = models.DateField(blank=True)

    def __unicode__(self):
        return "%s" % (str(self.Cliente) + " - " + str(self.LoteVenta) + " - " + str(self.FechaVenta))

class Persona(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    DNI = models.CharField(max_length=10, primary_key = True)
    Telefono = models.CharField(max_length=50, null = True)
    Email = models.EmailField(null = True)
    Baja = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "%s" % str(str(self.Nombre) + " - " + str(self.Apellido) + " - " + str(self.DNI))

class Productor (Persona):
    CUIL = models.CharField(max_length=13, primary_key = True)
        
    def __unicode__(self):
        return "%s" % str(str(self.Nombre) + " " + str(self.Apellido) + " - CUIL: " + str(self.CUIL))

class Representante(Persona): 
    NroLegajo = models.PositiveIntegerField(max_length=50, primary_key = True)
    Zona = models.CharField(max_length=50)
                
    def __unicode__(self):
        return "%s" % str(str(self.Nombre) + " " + str(self.Apellido) + " - DNI: " + str(self.DNI))

class Estancia(models.Model):
    Nombre   = models.CharField(max_length=50)
    CUIT = models.CharField(max_length=13, primary_key = True)
    Provincia = models.CharField(max_length=50)
    Zona = models.CharField(max_length=50)
    Baja = models.BooleanField(default=False)
    Representante = models.ForeignKey('Representante', null = True)
    Productor = models.OneToOneField('Productor', null = True)
    
    def __unicode__(self):
        return "%s" % str(str(self.Nombre) + " " + str(self.Provincia) + " " + str(self.CUIT) )


# First, define the Manager subclass.
class BajaLogicaManager(models.Manager):
    def __init__(self, **kwargs):
        super(BajaLogicaManager, self).__init__()
        self.kwargs = kwargs

    def get_queryset(self):
        return super(BajaLogicaManager, self).get_queryset().filter(**self.kwargs)

class Lote(models.Model):
    NroLote = models.AutoField(primary_key = True)
    CantFardos = models.PositiveIntegerField(max_length=50)
    Peso = models.PositiveIntegerField(max_length=50)
    Baja = models.BooleanField(default=False)
    Compra = models.OneToOneField('CompraLote')
    Estancia = models.ForeignKey('Estancia', null = True)

    objects = BajaLogicaManager()                   # Mostrar todos los objetos
    noEliminados = eliminados = BajaLogicaManager(Baja = False)     # Mostrar objetos con baja = false
    eliminados = BajaLogicaManager(Baja = True)     # Mostrar objetos con baja = true

    def __unicode__(self):
        return u"%s" % self.NroLote

class Fardo(models.Model):
    NroFardo = models.AutoField(primary_key = True)
    Lote = models.ForeignKey('Lote')
    TipoFardo = models.ForeignKey('TipoFardo')
    Peso = models.FloatField()
    Rinde = models.FloatField()
    Finura = models.FloatField()
    CV = models.FloatField()
    AlturaMedia = models.FloatField()
    Romana = models.FloatField()
    Cuadricula = models.ForeignKey('Cuadricula', null = True)
    DetalleOrden = models.ForeignKey('DetalleOrden', null = True)

    def __unicode__(self):
        return u"%d" % self.NroFardo

class TipoFardo(models.Model):
    Nombre = models.CharField(max_length=50, primary_key = True)
    Descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % (str(self.Nombre))


class OrdenProduccion(models.Model):
    NroOrden = models.AutoField(primary_key = True)
    FechaEmision = models.DateField(auto_now_add = True)
    CantRequerida = models.PositiveIntegerField(max_length=50)
    Servicio = models.ManyToManyField('Servicio')
    CV = models.FloatField()
    AlturaMedia = models.FloatField()
    Finura = models.FloatField() # Medida Micrones
    Romana = models.FloatField()
    FechaInicioProduccion = models.DateField(null = True) 
    FechaFinProduccion = models.DateField(null = True) 
    MaquinaActual = models.ForeignKey('Maquinaria', null = True)
    EnProduccion = models.BooleanField(default=False)
    Finalizada = models.BooleanField(default=False)
    Cancelada = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s" % (self.NroOrden, u", ".join([unicode(s) for s in self.Servicio.all()]))

class DetalleOrden(models.Model):
    NroDetalle = models.AutoField(primary_key = True)
    OrdenProduccion = models.ForeignKey('OrdenProduccion')
    
    def __unicode__(self):
        return u"Nro. Detalle: %s" % self.NroDetalle

class Servicio(models.Model):
    Nombre = models.CharField(max_length=50, primary_key = True)
    Descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s" % self.Nombre

class LoteVenta(models.Model):
    NroPartida = models.AutoField(primary_key = True)
    FechaCierreOrden = models.DateField() 
    Cantidad = models.PositiveIntegerField(max_length=50)
    Cuadricula = models.ForeignKey('Cuadricula')
    Baja = models.BooleanField(default=False)
    OrdenProduccion = models.OneToOneField('OrdenProduccion')
    
    objects = BajaLogicaManager(Baja = False)       # Mostrar objetos con baja = false
    eliminados = BajaLogicaManager(Baja = True)     # Mostrar objetos con baja = true

    def __unicode__(self):
        return "%s" % (str(self.NroPartida))

class Cuadricula(models.Model):
    NroCuadricula = models.AutoField(primary_key = True)

    def __unicode__(self):
        return "%s Cuadri" % self.NroCuadricula

class Maquinaria(models.Model):
    NroSerie = models.PositiveIntegerField(max_length=50, primary_key = True)
    TipoMaquinaria = models.OneToOneField('Servicio')
    Descripcion = models.CharField(max_length=50, null = True)

    def __unicode__(self):
        return u"%s - %s" % (self.NroSerie, self.TipoMaquinaria)
