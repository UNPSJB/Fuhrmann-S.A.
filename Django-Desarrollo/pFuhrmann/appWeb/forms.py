#encoding:utf-8
from django.forms import ModelForm
from django import forms
from appWeb.models import * 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

#REGISTRO DE OPERACION
class compraForm(forms.ModelForm):    
    class Meta:
        model = CompraLote
    
    def __init__(self, *args, **kwargs):
        super(compraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()   
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success", onClick="alert('Compra Registrada!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class ventaForm(forms.ModelForm):
    class Meta:
        model = Venta
    
    def __init__(self, *args, **kwargs):
        super(ventaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success",onClick="alert('Venta Registrada!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

#ESTANCIA
class registrarEstanciaForm(forms.ModelForm):
    class Meta:
        model = Estancia
        exclude = ['Baja']

    def __init__(self, *args, **kwargs):
        super(registrarEstanciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success",onClick="alert('Estancia Registrada!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class modificarEstanciaForm(forms.ModelForm):
    class Meta:
        model = Estancia
        
    def __init__(self, *args, **kwargs):
        super(modificarEstanciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Button('submit', 'Modificar', css_class="btn btn-default",onClick = "location.href='/listadoEstancias'"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

#LOTES&FARDOS
class registrarLoteForm(forms.ModelForm):    
    class Meta:
        model = Lote
        exclude = ("Baja",)

    def __init__(self, *args, **kwargs):
        super(registrarLoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success",onClick="alert('Lote Registrado!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default", onClick="location.href='/index'"))
    
class modificarLoteForm(forms.ModelForm):
    class Meta:
        model = Lote

    Peso = forms.IntegerField(label ="PesoLote", min_value = 0)
    CantFardos = forms.IntegerField(label ="CantidadFardos", min_value = 0)

    def __init__(self, *args, **kwargs):
        super(modificarLoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarLoteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Button('submit', 'Modificar', css_class="btn btn-default",onClick = "location.href='/listadoLotes'"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class registrarFardoForm(ModelForm):
    class Meta:
        model = Fardo
        exclude = ['Baja']
    
    def __init__(self, *args, **kwargs):
        super(registrarFardoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success", onClick="alert('Fardos Registrados!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class modificarFardoForm(forms.ModelForm):
    class Meta:
        model = Fardo

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
        self.helper.add_input(Button('submit', 'Modificar', css_class="btn btn-default",onClick = "location.href='/ListadoFardos'"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-success",onClick = "location.href='/index'"))

#PERSONAL
class registrarProductorForm(forms.ModelForm):
    class Meta:
        model = Productor
    
    def __init__(self, *args, **kwargs):
        super(registrarProductorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success", onClick="alert('Productor Registrado!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class modificarProductorForm(forms.ModelForm):
    class Meta:
        model = Productor

    def __init__(self, *args, **kwargs):
        super(modificarProductorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Button('submit', 'Modificar', css_class="btn btn-default",onClick = "location.href='/listadoProductores'"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class registrarRepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
    
    def __init__(self, *args, **kwargs):
        super(registrarRepresentanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success", onClick="alert('Representante Registrado!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class modificarRepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante

    def __init__(self, *args, **kwargs):
        super(modificarRepresentanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Button('submit', 'Modificar', css_class="btn btn-default",onClick = "location.href='/listadoRepresentante'"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

#PRODUCCION
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

#Maquinaria
class registrarMaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        exclude = ['Baja']
    
    def __init__(self, *args, **kwargs):
        super(registrarMaquinariaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Registrar', css_class="btn btn-success", onClick="alert('Maquinaria Registrada!')"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))

class modificarMaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        
    def __init__(self, *args, **kwargs):
        super(modificarMaquinariaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Button('submit', 'Modificar', css_class="btn btn-default",onClick = "location.href='/listadoMaquinaria'"))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "location.href='/index'"))
