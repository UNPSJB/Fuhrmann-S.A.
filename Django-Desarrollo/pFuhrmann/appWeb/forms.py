#encoding:utf-8
from django.forms import ModelForm
from django import forms
from appWeb.models import *
 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class compraForm(ModelForm):
    class Meta:
        model = CompraLote
        exclude = ['Registrada']
    def __init__(self, *args, **kwargs):
        super(compraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-compraForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class ventaForm(ModelForm):
    class Meta:
        model = Venta
    def __init__(self, *args, **kwargs):
        super(ventaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ventaForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class nuevaOrdenProduccionForm(ModelForm):
    class Meta:
        model = OrdenProduccion
        exclude = ['EnProduccion', 'Finalizada']
    def __init__(self, *args, **kwargs):
        super(nuevaOrdenProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-nuevaOrdenProduccionForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))
        self.helper.add_input(Submit('cancel', 'Cancel'))

class modificarOrdenProduccionForm(forms.Form):
    OrdenProduccion = forms.CharField(label ="NroOrdenProduccion", max_length = 50)
    def __init__(self, *args, **kwargs):
        super(modificarOrdenProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarOrdenProduccionForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class enviarFaseProduccionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(enviarFaseProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-enviarFaseProduccionForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class finalizarFaseProduccionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(finalizarFaseProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-finalizarFaseProduccionForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class registrarLoteForm(ModelForm):
    class Meta:
        model = Lote
        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarLoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarLoteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class modificarLoteForm(forms.Form):
    NroLote = forms.CharField(label ="NroLote", max_length = 50)
    def __init__(self, *args, **kwargs):
        super(modificarLoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarLoteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class registrarFardoForm(ModelForm):
    class Meta:
        model = Fardo
        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarFardoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarFardoForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class modificarFardoForm(forms.Form):
    NroFardo = forms.CharField(label ="NroFardo", max_length = 50)
    def __init__(self, *args, **kwargs):
        super(modificarFardoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarFardoForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class registrarEstanciaForm(ModelForm):
    class Meta:
        model = Estancia
        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarEstanciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarEstanciaForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class modificarEstanciaForm(forms.Form):

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
        self.helper.add_input(Submit('submit', 'Aceptar'))

class modificarProductorForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(modificarProductorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarProductorForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class registrarRepresentanteForm(ModelForm):
    class Meta:
        model = Representante
        exclude = ['Baja']
    def __init__(self, *args, **kwargs):
        super(registrarRepresentanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrarRepresentanteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))

class modificarRepresentanteForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(modificarRepresentanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modificarRepresentanteForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Aceptar'))
