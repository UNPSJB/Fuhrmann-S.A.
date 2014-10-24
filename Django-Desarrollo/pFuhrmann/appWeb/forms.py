#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from appWeb.models import * 
from localflavor.ar.forms import ARCUITField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

# ------------- Formulario de Compras
class CompraForm(forms.ModelForm):    
    FechaLlegada = forms.DateField(label = "Fecha de Llegada",widget = forms.TextInput(attrs = {'id':'datepicker'}), required = False) #Ejemplo Datepicker
    class Meta:
        model = CompraLote
    
    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()   

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

# ------------- Formulario de Ventas
class VentaForm(forms.ModelForm):
    LoteVenta = forms.ModelMultipleChoiceField(LoteVenta.objects.all(),label = "Lote Venta")
    FechaVenta = forms.DateField(label = "Fecha",widget = forms.TextInput(attrs = {'id':'datepicker'}), required = False) #Ejemplo Datepicker

    class Meta:
        model = Venta
    
    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

# ------------- Formularios de Estancia

class EstanciaForm(forms.ModelForm):
    # Override de Cuit
    CUIT = ARCUITField(label="El cuit", help_text="Un cuit")
    # Campo nuevo
    algo = forms.IntegerField()
    # Ver django-selectable para autocompletado
    class Meta:
        model = Estancia
        exclude = ['Baja']
        widgets = {
            'Zona': forms.Select(choices=[('Sur', 'Sur'), ('Norte', 'Norte')])
        }

    def __init__(self, *args, **kwargs):
        super(EstanciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean_algo(self):
        if self.cleaned_data['algo'] == 2:
            raise ValidationError("Algo no puede ser 2")
        return self.cleaned_data['algo']

    #def clean_CUIT(self):
     #   return int(self.cleaned_data['CUIT'].replace('-', ''))
        
    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))


#LOTES&FARDOS

# ------------- Formularios de Lotes


class LoteForm(forms.ModelForm):    
    class Meta:
        model = Lote
      #  if *args is None:
      #      exclude = ("Peso", "Baja", )
      #  else:
        exclude = ("Baja", )
    
    
    CantFardos = forms.IntegerField(label ="Cantidad de Fardos", min_value = 0)


    def __init__(self, *args, **kwargs):
        super(LoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))


# ------------- Formularios de Fardo


class FardoForm(ModelForm):
    class Meta:
        model = Fardo
        exclude = ['Baja', 'DetalleOrden']

   # if this.instance is not None:
   #     print "sad"
        
    Lote = forms.ModelChoiceField(Lote.objects.all(), label ="Lote de Fardos")
    TipoFardo = forms.ModelChoiceField(TipoFardo.objects.all(), label ="Tipo de Fardo")
    CV = forms.FloatField(label ="Coeficiente de Variacion", min_value = 0)
    AlturaMedia = forms.FloatField(label ="Altura Media", min_value = 0)
    Cuadricula = forms.ModelChoiceField(Cuadricula.objects.all(), label ="Cuadricula", required = False)

    def __init__(self, *args, **kwargs):
        super(FardoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
    
    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))


#PERSONAL

# ---------------Formularios de Productor

class ProductorForm(forms.ModelForm):
    class Meta:
        model = Productor
    
    def __init__(self, *args, **kwargs):
        super(ProductorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
    
    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))


# ---------------Formularios de Representante


class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        widgets = {
            'Zona': forms.Select(choices=[('Sur', 'Sur'), ('Norte', 'Norte')])
        }
    
    def __init__(self, *args, **kwargs):
        super(RepresentanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))



#PRODUCCION

# ---------------Formularios de Orden de Produccion


class nuevaOrdenProduccionForm(forms.ModelForm):
    class Meta:
        model = OrdenProduccion
        exclude = ['EnProduccion', 'Finalizada', 'MaquinaActual']
    
    def __init__(self, *args, **kwargs):
        super(nuevaOrdenProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success",onClick = "alert('Orden de produccion Registrada!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class modificarOrdenProduccionForm(forms.ModelForm):
    Servicios = forms.ModelMultipleChoiceField(Servicio.objects.all())
    class Meta:
        model = OrdenProduccion

    def __init__(self, *args, **kwargs):
        super(modificarOrdenProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Button('submit', 'Modificar', css_class="btn btn-default",onClick = "location.href='/listadoOrden'"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-success",onClick = "location.href='/index'"))

class enviarFaseProduccionForm(forms.ModelForm):
    class Meta:
        model = OrdenProduccion

    def __init__(self, *args, **kwargs):
        super(enviarFaseProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-success",onClick = "location.href='/index'"))

class finalizarFaseProduccionForm(forms.ModelForm):
    class Meta:
        model = OrdenProduccion
    
    def __init__(self, *args, **kwargs):
        super(finalizarFaseProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Button('submit', 'Finalizar'))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-success",onClick = "location.href='/index'"))

#-----------------Formularios de Maquinaria
class MaquinariaForm(forms.ModelForm):
    NroSerie = forms.IntegerField(label = "Nro. Serie",required=False)
    Descripcion = forms.CharField(required = False)
    TipoMaquinaria = forms.ModelMultipleChoiceField(Servicio.objects.all(), label = "Servicio")
    class Meta:
        model = Maquinaria
        exclude = ['Baja']
    
    def __init__(self, *args, **kwargs):
        super(MaquinariaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))
