#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from appWeb.models import * 
from localflavor.ar.forms import ARCUITField
from localflavor.ar.forms import ARDNIField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField


# ********************************* Login *********************************
class LoginForm(forms.Form):
    username = forms.CharField(label = "Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label = "Contraseña") 
    

# ********************************* Formulario de Compras *********************************
class CompraForm(forms.ModelForm):    
    FechaLlegada = forms.DateField(label = "Fecha de Llegada (*)",widget = forms.TextInput(attrs = {'id':'datepicker'})) #Ejemplo Datepicker
    Estancia = forms.ModelChoiceField(Estancia.objects.all(),label= "Estancia (*)")
    Representante = forms.ModelChoiceField(Representante.objects.all(), label="Representante (*)")
    class Meta:
        model = CompraLote
    
    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()   
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(

            Fieldset( 
                '<font color = "Black" size=3 face="Comic Sans MS">Datos de compra</font>',
                Field('Representante', css_class= ".col-lg-3",placeholder='Representante'),
                Field('Estancia', placeholder="Estancia"),
                Field('FechaLlegada', placeholder="Fecha de llegada"),
            ),
            
            HTML('<p>(*)Campos obligatorios.</p>'),
        )

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

# ********************************* Formulario de Ventas *********************************
class VentaForm(forms.ModelForm):
    LoteVenta = forms.ModelChoiceField(LoteVenta.objects.all(),label = "Lote Venta (*)")
    Cliente = forms.CharField(label= "Cliente (*)")
    FechaVenta = forms.DateField(label = "Fecha Venta (*)",widget = forms.TextInput(attrs = {'id':'datepicker'})) #Ejemplo Datepicker

    class Meta:
        model = Venta
    
    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(

            Fieldset( 
                '<font color = "Black" size=3 face="Comic Sans MS">Datos de Venta</font>',
                Field('LoteVenta', css_class= ".col-lg-3",placeholder='Lote de venta'),
                Field('Cliente', placeholder="Cliente"),
                Field('FechaVenta', placeholder="Fecha de venta"),
            ),
            
            HTML('<p>(*)Campos obligatorios.</p>'),
        )


    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

# ********************************* Formularios de Estancia *********************************


def EstanciaFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros

    class EstanciaForm(forms.ModelForm):

        Nombre = forms.CharField(label="Nombre (*)")

        class Meta:
            model = Estancia
            exclude = ['Baja']
       
            widgets = {
                'Zona': forms.Select(choices=[('Sur', 'Sur'), ('Norte', 'Norte')]), 
                'Provincia': forms.Select(choices=[('Chubut', 'Chubut'), ('Santa Cruz', 'Santa Cruz'), ('Buenos Aires', 'Buenos Aires')])
            }

        if not edit:
            CUIT = ARCUITField(label="CUIT (*)")
            Representante = forms.ModelChoiceField(Representante.objects.all(), label="Representante (*)")
            Productor= forms.ModelChoiceField(Productor.objects.all(),label="Productor (*)")
        else:
            CUIT = ARCUITField(label="CUIT (*)", widget=forms.HiddenInput())
            Representante = forms.ModelChoiceField(Representante.objects.all(), label="Representante (*)",widget=forms.HiddenInput())
            Productor= forms.ModelChoiceField(Productor.objects.all(),label="Productor (*)",widget=forms.HiddenInput())



        def __init__(self, *args, **kwargs):
            super(EstanciaForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(
        
                Fieldset( 
                    '<font color = "Black" size=3 face="Comic Sans MS">Datos de Estancia </font>',
                    Field('Nombre', placeholder="Nombre"),
                    Field('CUIT', placeholder="CUIT  XX-XXXXXXXX-X"),
                    Field('Provincia'),
                    Field('Zona'),
                    Field('Representante'),
                    Field('Productor'),
                ),
                HTML('<p>(*)Campos obligatorios.</p>'),
            )    

        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submit', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

    return EstanciaForm


#LOTES&FARDOS

# ********************************* Formularios de Lotes *********************************

def LoteFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros

    class LoteForm(forms.ModelForm):    
        
        class Meta:
            model = Lote
            exclude = ("Baja", "Estancia")
  
        CantFardos = forms.IntegerField(label ="Cantidad de Fardos (*)", min_value = 0)
        Peso = forms.IntegerField(label ="Peso del Lote (*)", min_value = 0)
        
        if not edit:
            Compra = forms.ModelChoiceField(CompraLote.objects.all().filter(lote = None), label ="Compra del Lote (*)")
        else:
            Compra = forms.ModelChoiceField(CompraLote.objects.all(), label ="Compra del Lote (*)", widget=forms.HiddenInput())

        def __init__(self, *args, **kwargs):
            super(LoteForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(
            
                Fieldset( 
                    '<font color = "Black" size=3 face="Comic Sans MS">Datos Principales </font>',
                    Field('CantFardos', placeholder="Cantidad de fardos"),
                    Field('Peso', placeholder="Peso del lote"),
                    Field('Compra'),
                ),
                HTML('<p>(*)Campos obligatorios.</p>'),
            )

        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submit', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))
        
        def clean_Peso(self):
            peso = self.cleaned_data['Peso']
            cantidad =  self.cleaned_data['CantFardos']
            
            if ( ( peso / cantidad ) < 280 ) or ( ( peso / cantidad ) > 300 ):
                raise ValidationError("El Peso debe ser 280-300kg por Fardo")
            return peso
    
    return LoteForm


# ********************************* Formularios de Fardo *********************************

def FardoFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros
    class FardoForm(ModelForm):
        class Meta:
            model = Fardo
            exclude = ['Baja', 'DetalleOrden']

        if edit:
            Lote = forms.ModelChoiceField(Lote.eliminados.all(), label ="Lote de Fardos (*)", widget=forms.HiddenInput())
            Cuadricula = forms.ModelChoiceField(Cuadricula.objects.all(), label ="Cuadricula ", required = False, widget=forms.HiddenInput())
        else:
            Lote = forms.ModelChoiceField(Lote.noEliminados.all(), label ="Lote de Fardos (*)")
            Cuadricula = forms.ModelChoiceField(Cuadricula.objects.all(), label ="Cuadricula ", required = False)

        TipoFardo = forms.ModelChoiceField(TipoFardo.objects.all(), label ="Tipo de Fardo (*)")
        CV = forms.FloatField(label ="C. Variacion (*)", min_value = 0)
        AlturaMedia = forms.FloatField(label ="Altura Media (*)", min_value = 0)
        Peso = forms.FloatField(label ="Peso (*)", min_value = 0)
        Rinde = forms.FloatField(label ="Rinde (*)", min_value = 0)
        Finura = forms.FloatField(label ="Finura (*)", min_value = 0)
        Romana = forms.FloatField(label ="Romana (*)", min_value = 0)

        def __init__(self, *args, **kwargs):
            super(FardoForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(

                Fieldset( 
                    '<font color = "Black" size=3 face="Comic Sans MS">Datos Principales </font>',
                    Field('Lote', css_class= ".col-lg-3",placeholder='asd'),
                    Field('TipoFardo', placeholder="Tipo de Fardos"),
                ),
                Fieldset(
                    '<font color = "Black" size=3 face="Comic Sans MS">Especificaciones</font>',
                    Field('Peso', placeholder="Peso"),
                    Field('Rinde', placeholder="Rinde"),
                    Field('Finura', placeholder="Finura"),
                    Field('CV', placeholder="Coeficiente de Variacion"),
                    Field('AlturaMedia', placeholder="Altura Media"),
                    Field('Romana', placeholder="Romana"),
                ),
                Fieldset(
                    '<font color = "Black" size=3 face="Comic Sans MS">Ubicacion</font>',
                    Field('Cuadricula', placeholder="Ubicacion en Cuadricula"),
                ),
                
                HTML('<p>(*)Campos obligatorios.</p>'),
            )

        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submit', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))
    return FardoForm

#PERSONAL

# ********************************* Formularios de Productor *********************************

def ProductorFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros

    class ProductorForm(forms.ModelForm):
        
        Nombre = forms.CharField(label="Nombre (*)")
        Apellido = forms.CharField(label="Apellido (*)" )

        class Meta:
            model = Productor
            exclude = ['Baja']

        Telefono = forms.CharField(label = "Telefono", required = False)
        Email = forms.CharField(label = "Email", required = False)


        if edit:
            DNI = ARDNIField(label="DNI (*)")
            CUIL = ARCUITField(label="CUIL (*)")
        else:
            DNI = ARDNIField(label="DNI (*)",widget=forms.HiddenInput())
            CUIL = ARCUITField(label="CUIL (*)",widget=forms.HiddenInput())


        def __init__(self, *args, **kwargs):
            super(ProductorForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(

                Fieldset( 
                    '<font color = "Black" size=3 face="Arial">Datos Obligatorios </font>',
                    Field('Nombre', css_class= ".col-lg-3",placeholder='Nombre'),
                    Field('Apellido', placeholder="Apellido"),
                    Field('DNI', placeholder="DNI"),
                    Field('CUIL', placeholder="CUIL XX-XXXXXXXX-X"),
                ),
                Fieldset(
                    '<font color = "Black" size=3 face="Arial">Datos Opcionales</font>',
                    Field('Telefono', placeholder="Telefono"),
                    Field('Email', placeholder="Email"),
                ),
            )

    #def clean_CUIL(self):
    #    return int(self.cleaned_data['CUIL'].replace('-', ''))        

        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submibl', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

    return ProductorForm

# ********************************* Formularios de Representante *********************************

def RepresentanteFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros

    class RepresentanteForm(forms.ModelForm):
        
        Nombre = forms.CharField(label="Nombre (*)")
        Apellido = forms.CharField(label="Apellido (*)")
    
        class Meta:
            exclude = ['Baja']
            model = Representante
            widgets = {
           'Zona': forms.Select(choices=[('Sur', 'Sur'), ('Norte', 'Norte')])
            }

            Telefono = forms.CharField(label = "Telefono", required = False)
            Email = forms.CharField(label = "Email", required = False)


        if not edit:
            NroLegajo = forms.IntegerField(label ="Nro.Legajo (*)")
            DNI = ARDNIField(label="DNI (*)")
        else:
            NroLegajo = forms.IntegerField(label ="Nro.Legajo (*)", widget=forms.HiddenInput())
            DNI = ARDNIField(label="DNI (*)",  widget=forms.HiddenInput())
 
        def __init__(self, *args, **kwargs):
            super(RepresentanteForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(

                Fieldset( 
                    '<font color = "Black" size=3 face="Arial">Datos Obligatorios </font>',
                    Field('Nombre', css_class= ".col-lg-3",placeholder='Nombre'),
                    Field('Apellido', placeholder="Apellido"),
                    Field('DNI', placeholder="DNI"),
                    Field('NroLegajo', placeholder="Nro de Legajo"),
                ),
                Fieldset(
                    '<font color = "Black" size=3 face="Arial">Datos Opcionales</font>',
                    Field('Telefono', placeholder="Telefono"),
                    Field('Email', placeholder="Email"),
                    Field('Zona', placeholder="Zona"),
                ),
            )

        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submit', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

    return RepresentanteForm



#PRODUCCION

# ********************************* Formularios de Orden de Produccion *********************************


class OrdenProduccionForm(forms.ModelForm):
    
    class Meta:
        model = OrdenProduccion
        exclude = ['EnProduccion', 'Finalizada', 'MaquinaActual', 'FechaFinProduccion', 'FechaInicioProduccion']

    CantRequerida = forms.IntegerField(label = "Cantidad Requerida (*)", min_value = 0)
    CV = forms.FloatField(label ="C. Variacion (*)", min_value = 0)
    AlturaMedia = forms.FloatField(label ="Altura Media (*)", min_value = 0)
    Finura = forms.FloatField(label ="Finura (*)", min_value = 0)        # Unidad de Medida Micrones
    Romana = forms.FloatField(label ="Romana (*)", min_value = 0)
    Servicio = forms.ModelMultipleChoiceField(Servicio.objects.all(), label ="Servicios a Realizar (*)")

    def __init__(self, *args, **kwargs):
        super(OrdenProduccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(

            Fieldset( 
                '<font color = "Black" size=3 face="Comic Sans MS">Datos Primarios de Orden de Produccion </font>',
                Field('CantRequerida', placeholder="Cantidad en Kilos requeridos"),
                Field('Servicio', placeholder="Servicios a Realizar"),
            ),
            Fieldset(
                '<font color = "Black" size=3 face="Comic Sans MS">Especificaciones de Orden de Produccion</font>',
                Field('CV', placeholder="Coeficiente de Variacion requerido"),
                Field('AlturaMedia', placeholder="Altura Media requerida"),
                Field('Finura', placeholder="Micronaje requerido"),
                Field('Romana', placeholder="Romana requerida"),
            ),
            HTML('<p>(*)Campos obligatorios.</p>'),
        )

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))



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



# ********************************* Formularios de Maquinaria *********************************

class MaquinariaForm(forms.ModelForm):
    NroSerie = forms.IntegerField(label = "Nro. Serie (*)")
    Descripcion = forms.CharField(required = False)
    TipoMaquinaria = forms.ModelChoiceField(Servicio.objects.all(), label = "Servicio (*)")
    class Meta:
        model = Maquinaria
        exclude = ['Baja']
    
    def __init__(self, *args, **kwargs):
        super(MaquinariaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset( 
                '<font color = "Black" size=3 face="Comic Sans MS">Datos de Maquinaria</font>',
                Field('NroSerie', css_class= ".col-lg-3",placeholder='Nro de Serie'),
                Field('TipoMaquinaria'),
                Field('Descripcion', placeholder="Descripcion"),
            ),
            
            HTML('<p>(*)Campos obligatorios.</p>'),
        )

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar',css_class="btn btn-default",onClick = "history.back()"))
