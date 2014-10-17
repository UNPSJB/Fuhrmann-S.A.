from django.db import models

class CompraLote(models.Model):
    NroCompra = models.AutoField(primary_key = True)
    Representante = models.ForeignKey('Representante')
    Estancia = models.ForeignKey('Estancia')
    FechaLlegada = models.DateField()
    
    def __unicode__(self):
        return "%s" % (str(self.NroCompra) + " " + str(self.FechaLlegada))

class Venta(models.Model):
    NroVenta = models.AutoField(primary_key = True)
    LoteVenta = models.OneToOneField('LoteVenta')
    Cliente = models.CharField(max_length=50)
    FechaVenta = models.DateField(blank=True)

    def __unicode__(self):
        return ""

class Persona(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    DNI = models.CharField(max_length=50, primary_key = True)
    Telefono = models.CharField(max_length=50, null = True)
    Email = models.EmailField(null = True)
    Baja = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "%s" % str(str(self.Nombre) + " " + str(self.Apellido))

class Productor (Persona):
    CUIL = models.CharField(max_length=50, primary_key = True)
        
    def __unicode__(self):
        return "%s" % str(str(self.Nombre) + " " + str(self.Apellido))

class Representante(Persona): 
    NroLegajo = models.PositiveIntegerField(max_length=50, primary_key = True)
    Zona = models.CharField(max_length=50)
                
    def __unicode__(self):
        return "%s" % str(str(self.NroLegajo) + " " + str(self.Nombre) + " " + str(self.Apellido))

class Estancia(models.Model):
    Nombre = models.CharField(max_length=50)
    CUIT = models.CharField(max_length=13, primary_key = True)
    Provincia = models.CharField(max_length=50)
    Zona = models.CharField(max_length=50)
    Baja = models.BooleanField(default=False)
    Representante = models.ForeignKey('Representante', null = True)
    Productor = models.OneToOneField('Productor', null = True)
    
    def __unicode__(self):
        return "%s" % str(str(self.Nombre) + " " + str(self.Provincia))

# First, define the Manager subclass.
class BajaLogicaManager(models.Manager):
    def __init__(self, **kwargs):
        super(BajaLogicaManager, self).__init__()
        self.kwargs = kwargs

    def get_queryset(self):
        return super(BajaLogicaManager, self).get_queryset().filter(**self.kwargs)

class Lote(models.Model):
    NroLote = models.AutoField(primary_key = True)
    Peso = models.PositiveIntegerField(max_length=50)
    CantFardos = models.PositiveIntegerField(max_length=50)
    Baja = models.BooleanField(default=False)

    objects = BajaLogicaManager(Baja = False)
    elimindos = BajaLogicaManager(Baja = True)
    def __unicode__(self):
        return ""

class Fardo(models.Model):
    NroFardo = models.AutoField(primary_key = True)
    TipoFardo = models.ForeignKey('TipoFardo')
    Peso = models.FloatField()
    Rinde = models.FloatField()
    Finura = models.FloatField()
    CV = models.FloatField()
    AlturaMedia = models.FloatField()
    Micronaje = models.FloatField()
    Romana = models.FloatField()
    Cuadricula = models.ForeignKey('Cuadricula', null = True)
    DetalleOrden = models.ForeignKey('DetalleOrden', null = True)
    Compra = models.OneToOneField('CompraLote')

    def __unicode__(self):
        return ""

class TipoFardo(models.Model):
    Nombre = models.CharField(max_length=50, primary_key = True)
    Descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return ""


class OrdenProduccion(models.Model):
    NroOrden = models.AutoField(primary_key = True)
    FechaEmision = models.DateField(auto_now_add = True)
    CantRequerida = models.PositiveIntegerField(max_length=50)
    Servicio = models.ManyToManyField('Servicio')
    CV = models.FloatField()
    AlturaMedia = models.FloatField()
    Micronaje = models.FloatField()
    Romana = models.FloatField()
    FechaInicioProduccion = models.DateField(null = True) 
    FechaFinProduccion = models.DateField(null = True) 
    MaquinaActual = models.ForeignKey('Maquinaria', null = True)
    EnProduccion = models.BooleanField(default=False)
    Finalizada = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s" % (self.NroOrden, u", ".join([unicode(s) for s in self.Servicio.all()]))

class DetalleOrden(models.Model):
    NroDetalle = models.AutoField(primary_key = True)
    OrdenProduccion = models.OneToOneField('OrdenProduccion')
    Fardo = models.OneToOneField('Fardo') #Cuando se crea el detalle, tiene que tener asociado 1 fardo
    def __unicode__(self):
        return ""

class Servicio(models.Model):
    Nombre = models.CharField(max_length=50, primary_key = True)
    Descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s" % (self.Nombre)

class LoteVenta(models.Model):
    NroPartida = models.AutoField(primary_key = True)
    ServicioRealizado = ('Lavado', 'Peinado', 'Cardado')
    FechaCierreOrden = models.DateField() 
    Cantidad = models.PositiveIntegerField(max_length=50)
    Cuadricula = models.ForeignKey('Cuadricula')
    Servicio = models.ManyToManyField('Servicio')
    Baja = models.BooleanField(default=False)
    OrdenProduccion = models.OneToOneField('OrdenProduccion')
    
    def __unicode__(self):
        return ""

class Cuadricula(models.Model):
    NroCuadricula = models.AutoField(primary_key = True)

    def __unicode__(self):
        return ""

class Maquinaria(models.Model):
    NroSerie = models.PositiveIntegerField(max_length=50, primary_key = True)
    TipoMaquinaria = models.OneToOneField('Servicio')
    Descripcion = models.CharField(max_length=50, null = True)

    def __unicode__(self):
        return u"%s - %s" % (self.tipoMaquinaria, self.NroSerie)
