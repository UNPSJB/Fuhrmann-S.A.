#encoding:utf-8
from django.forms import ModelForm
from django import forms
from appWeb.models import *

 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class compraForm(forms.Form):
    Representante = forms.ModelChoiceField(Representante.objects.all())
    Estancia = forms.ModelChoiceField(Estancia.objects.all())
    FechaLlegada = forms.DateField(label = "Fecha de Llegada")

    def __init__(self, *args, **kwargs):
        super(compraForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_id = 'id-compraForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))


class ventaForm(forms.Form):
    FechaVenta = forms.DateField(label = "Fecha de Venta")
    Cliente = forms.CharField(label ="Cliente", max_length = 50)
    LoteVenta = forms.ModelChoiceField(LoteVenta.objects.all(), label = "Lote Venta")
    
    def __init__(self, *args, **kwargs):
        super(ventaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ventaForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class nuevaOrdenProduccionForm(ModelForm):
    class Meta:
        model = OrdenProduccion
        exclude = ['EnProduccion', 'Finalizada', 'MaquinaActual']
    def __init__(self, *args, **kwargs):
        super(nuevaOrdenProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-nuevaOrdenProduccionForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class modificarOrdenProduccionForm(forms.Form):
    Servicios = forms.ModelMultipleChoiceField(Servicio.objects.all())
    def __init__(self, *args, **kwargs):
        super(modificarOrdenProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarOrdenProduccionForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Modificar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class enviarFaseProduccionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(enviarFaseProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-enviarFaseProduccionForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class finalizarFaseProduccionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(finalizarFaseProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-finalizarFaseProduccionForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Button('submit', 'Finalizar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class registrarLoteForm(forms.Form):
    Peso = forms.IntegerField(label ="Peso Lote", min_value = 0)
    CantFardos = forms.IntegerField(label ="Cantidad Fardos", min_value = 0)
    date = forms.DateField(widget = forms.TextInput(attrs = {'id':'datepicker'}), required = False) #Ejemplo Datepicker
    # required = False, es para que no se lo pida como obligatorio
    
    def __init__(self, *args, **kwargs):
        super(registrarLoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarLoteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-success", onClick="alert('asd');"))
        
class modificarLoteForm(forms.Form):
    Peso = forms.IntegerField(label ="PesoLote", min_value = 0)
    CantFardos = forms.IntegerField(label ="Cant.Fardos", min_value = 0)

    def __init__(self, *args, **kwargs):
        super(modificarLoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarLoteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Modificar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))        

class registrarFardoForm(ModelForm):
    class Meta:
        model = Fardo
        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarFardoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarFardoForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class modificarFardoForm(forms.Form):
    Tipo = forms.ModelChoiceField(TipoFardo.objects.all())
    Peso = forms.IntegerField(label ="Peso", min_value = 0)
    Rinde = forms.IntegerField(label ="Rinde", min_value = 0)
    Finura = forms.IntegerField(label ="Finura", min_value = 0)
    CoeficienteVariacion = forms.IntegerField(label ="CoeficienteVariacion", min_value = 0)
    AlturaMedia = forms.IntegerField(label ="AlturaMedia", min_value = 0)
    Micronaje = forms.IntegerField(label ="Micronaje", min_value = 0)
    Romana = forms.IntegerField(label ="Romana", min_value = 0)

    def __init__(self, *args, **kwargs):
        super(modificarFardoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarFardoForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout ('email', 
                                     'password',
                                     'remember_me',)

        self.helper.add_input(Submit('submit', 'Modificar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class registrarEstanciaForm(ModelForm):
    class Meta:
        model = Estancia

        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarEstanciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarEstanciaForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class modificarEstanciaForm(forms.Form):
    Nombre = forms.CharField(label ="Nombre", max_length = 50)
    Zona = forms.CharField(label ="Zona", max_length = 50)
    Provincia = forms.CharField(label ="Provincia", max_length = 50)
    def __init__(self, *args, **kwargs):
        super(modificarEstanciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarEstanciaForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class registrarProductorForm(ModelForm):
    class Meta:
        model = Productor
        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarProductorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarProductorForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class modificarProductorForm(forms.Form):
    Nombre = forms.CharField(label ="Nombre", max_length = 50)
    Apellido = forms.CharField(label ="Apellido", max_length = 50)
    Telefono = forms.CharField(label ="Telefono", max_length = 50)
    Email = forms.EmailField(label ="Email", max_length = 50)

    def __init__(self, *args, **kwargs):
        super(modificarProductorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarProductorForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Modificar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class registrarRepresentanteForm(ModelForm):
    class Meta:
        model = Representante
        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarRepresentanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarRepresentanteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class modificarRepresentanteForm(forms.Form):
    Nombre = forms.CharField(label ="Nombre", max_length = 50)
    Apellido = forms.CharField(label ="Apellido", max_length = 50)
    Telefono = forms.CharField(label ="Telefono", max_length = 50)
    Email = forms.EmailField(label ="Email", max_length = 50)
    Zona = forms.CharField(label ="Zona", max_length = 50)

    def __init__(self, *args, **kwargs):
        super(modificarRepresentanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarRepresentanteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class registrarMaquinariaForm(ModelForm):
    class Meta:
        model = Maquinaria
        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarMaquinariaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarMaquinariaForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))

class modificarMaquinariaForm(forms.Form):
    Tipo = forms.ModelChoiceField(Servicio.objects.all())
    Descripcion = forms.CharField(label ="Descripción", max_length = 50)

    def __init__(self, *args, **kwargs):
        super(modificarMaquinariaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarMaquinariaForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Modificar'))
        self.helper.add_input(Submit('cancel', 'Cancelar'))
