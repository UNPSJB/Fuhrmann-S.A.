from django.db import models

class CompraLote(models.Model):
    class Meta:
        ordering = ['NroCompra']
    NroCompra = models.AutoField(primary_key = True)
    Representante = models.ForeignKey('Representante')
    Estancia = models.ForeignKey('Estancia')
    FechaLlegada = models.DateField()
    
    def __unicode__(self):
        return "%s" % (str(self.Estancia) + " - " + str(self.FechaLlegada))

class Venta(models.Model):
    class Meta:
        ordering = ['NroVenta']
    NroVenta = models.AutoField(primary_key = True)
    LoteVenta = models.OneToOneField('LoteVenta')
    Cliente = models.CharField(max_length=50)
    FechaVenta = models.DateField()

    def __unicode__(self):
        return "%s" % (str(self.Cliente) + " - " + str(self.LoteVenta) + " - " + str(self.FechaVenta))

class Persona(models.Model):
    class Meta:
        ordering = ['Apellido']
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    DNI = models.CharField(max_length=10, primary_key = True)
    Telefono = models.CharField(max_length=50, null = True, blank = True)
    Email = models.EmailField(null = True, blank = True)
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
    class Meta:
        ordering = ['Nombre']
    
    Nombre = models.CharField(max_length=50)
    CUIT = models.CharField(max_length=13, primary_key = True)
    Provincia = models.CharField(max_length=50)
    Zona = models.CharField(max_length=50)
    Baja = models.BooleanField(default=False)
    Representante = models.ForeignKey('Representante')
    Productor = models.OneToOneField('Productor')
    
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
    class Meta:
        ordering = ['NroLote']    
    NroLote = models.AutoField(primary_key = True)
    TipoFardo = models.ForeignKey('TipoFardo')
    CantFardos = models.PositiveIntegerField(max_length=50)
    Peso = models.PositiveIntegerField(max_length=50)
    Baja = models.BooleanField(default=False)
    Compra = models.OneToOneField('CompraLote')
    Estancia = models.ForeignKey('Estancia')
    Cuadricula = models.CharField(max_length=50)

    objects = BajaLogicaManager()                                   # Mostrar todos los objetos
    noEliminados = eliminados = BajaLogicaManager(Baja = False)     # Mostrar objetos con baja = false
    eliminados = BajaLogicaManager(Baja = True)                     # Mostrar objetos con baja = true

    def __unicode__(self):
        return u"%s" % self.NroLote
  
class Fardo(models.Model):
    class Meta:
        ordering = ['NroFardo']
    NroFardo = models.AutoField(primary_key = True)
    Lote = models.ForeignKey('Lote')
    Peso = models.FloatField()
    Rinde = models.FloatField()
    Finura = models.FloatField()
    CV = models.FloatField()
    AlturaMedia = models.FloatField()
    Romana = models.FloatField()
    DetalleOrden = models.ForeignKey('DetalleOrden', null = True, blank = True)

    def __unicode__(self):
        return u"%d" % self.NroFardo

class TipoFardo(models.Model):
    Nombre = models.CharField(max_length=50, primary_key = True)
    Descripcion = models.CharField(max_length=50)
    Baja = models.BooleanField(default = False)
    
    def __unicode__(self):
        return "%s" % (str(self.Nombre))



# ************************ Orden de Produccion ***************************** #


class OrdenProduccion(models.Model):
    class Meta:
        ordering = ['NroOrden']
    NroOrden = models.AutoField(primary_key = True)
    FechaEmision = models.DateField(auto_now_add = True)
    CantRequerida = models.PositiveIntegerField(max_length=50)
    Servicio = models.ManyToManyField('Servicio', through='Produccion', null = True, blank = True)
    CV = models.FloatField()
    AlturaMedia = models.FloatField()
    Finura = models.FloatField()                                # Medida Micrones
    Romana = models.FloatField()
    Rinde = models.FloatField()
    Finalizada = models.BooleanField(default=False)
    Cancelada = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s " % self.NroOrden

    def isFinalizada(self):
        return all(map(lambda p: p.FechaFin != None, self.produccion_set.all()))
   
    def fechaFin(self):
        p = self.produccion_set.last()
        
        if p.FechaFin != None:
            return p.FechaFin
        
        return 'No Fecha'

    def fechaInicio(self):
        for p in self.produccion_set.all():
            if p.FechaInicio != None:
                return p.FechaInicio
        return 'No Fecha'

    def maquinaActual(self):
        maquinaActual = 'No Maquina'  
        for p in self.produccion_set.all():
            if p.FechaInicio != None  and  p.FechaFin == None:
                maquinaActual = p.Maquinaria.NroSerie
        return maquinaActual

    def isProduccion(self):
        isPro = False

        for p in self.produccion_set.all():
            print p.FechaFin
            if (p.FechaInicio != None) and (p.FechaFin != None):
                isPro = False
            elif (p.FechaInicio == None) and (p.FechaFin == None):
                isPro = False
        return isPro







class DetalleOrden(models.Model):
    class Meta:
        ordering = ['NroDetalle']
    NroDetalle = models.AutoField(primary_key = True)
    OrdenProduccion = models.ForeignKey('OrdenProduccion')
    
    def __unicode__(self):
        return u"Nro. Detalle: %s" % self.NroDetalle


class Servicio(models.Model):
    Nombre = models.CharField(max_length=50, primary_key = True)
    Descripcion = models.CharField(max_length=50)
    ServicioPrevio = models.ForeignKey('Servicio', blank = True, null = True)
    Transitorio = models.BooleanField(default = False)
    Baja = models.BooleanField(default = False)

    def __unicode__(self):
        return u"%s" % self.Nombre


class Produccion(models.Model):
    class Meta:
        ordering = ['NroProduccion']
    NroProduccion = models.AutoField(primary_key = True)
    Orden = models.ForeignKey('OrdenProduccion')
    Servicio = models.ForeignKey('Servicio')
    FechaInicio = models.DateField(null = True, blank = True)
    FechaFin = models.DateField(null = True, blank = True)
    Maquinaria = models.ForeignKey('Maquinaria', null = True, blank = True)

    def __unicode__(self):
        return u"%s" % self.NroProduccion


class Maquinaria(models.Model):
    class Meta:
        ordering = ['NroSerie']
    NroSerie = models.PositiveIntegerField(max_length=50, primary_key = True)
    Servicio = models.ForeignKey('Servicio')
    Descripcion = models.CharField(max_length=50, null = True, blank = True)
    Baja = models.BooleanField(default=False)
 
    def __unicode__(self):
        return u"%s " % (self.NroSerie)





# ***************************************************************************************** #


class LoteVenta(models.Model):
    class Meta:
        ordering = ['NroPartida']
    NroPartida = models.AutoField(primary_key = True)
    Cantidad = models.PositiveIntegerField(max_length=50)
    Cuadricula = models.CharField(max_length=50)
    Baja = models.BooleanField(default=False)
    OrdenProduccion = models.OneToOneField('OrdenProduccion')
    
    objects = BajaLogicaManager(Baja = False)       # Mostrar objetos con baja = false
    eliminados = BajaLogicaManager(Baja = True)     # Mostrar objetos con baja = true

    def __unicode__(self):
        return "%s" % (str(self.NroPartida))

