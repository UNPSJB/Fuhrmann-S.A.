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
    Estancia = forms.ModelChoiceField(Estancia.objects.filter(Baja = False),label= "Estancia (*)")
    Representante = forms.ModelChoiceField(Representante.objects.filter(Baja = False), label="Representante (*)")
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
    def clean_Estancia(self):
        representante = self.cleaned_data['Representante']
        estancia = self.cleaned_data['Estancia']
            
        if (representante != estancia.Representante):
            raise ValidationError("Esta estancia no corresponde con el representante.")
        return estancia

    def setup(self, *args, **kwarg):
        self.helper.add_input(Submit('submit', *args, **kwarg))
        self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

# ********************************* Formulario de Ventas *********************************
class VentaForm(forms.ModelForm):
    LoteVenta = forms.ModelChoiceField(LoteVenta.objects.all(),label = "Lote venta (*)")
    Cliente = forms.CharField(label= "Cliente (*)")
    FechaVenta = forms.DateField(label = "Fecha de venta (*)",widget = forms.TextInput(attrs = {'id':'datepicker'})) #Ejemplo Datepicker

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
                '<font color = "Black" size=3 face="Comic Sans MS">Datos de venta</font>',
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

        class Meta:
            model = Estancia
            exclude = ['Baja']
            widgets = {
                'Zona': forms.Select(choices=[('Sur', 'Sur'), ('Norte', 'Norte')]), 
                'Provincia': forms.Select(choices=[('Chubut', 'Chubut'), ('Santa Cruz', 'Santa Cruz'), ('Buenos Aires', 'Buenos Aires')])
            }
            
        Nombre = forms.CharField(label="Nombre (*)")
    
        if not edit:
            CUIT = ARCUITField(label="CUIT (*)")
            Representante = forms.ModelChoiceField(Representante.objects.filter(Baja = False), label="Representante (*)")
            Productor = forms.ModelChoiceField(Productor.objects.all().filter(Baja = False, estancia = None),label="Productor (*)")
        else:
            CUIT = ARCUITField(label="CUIT (*)", widget=forms.HiddenInput())
            Representante = forms.ModelChoiceField(Representante.objects.filter(Baja = False), label="Representante (*)", widget=forms.HiddenInput())
            Productor= forms.ModelChoiceField(Productor.objects.filter(Baja = False),label="Productor (*)", widget=forms.HiddenInput())



        def __init__(self, *args, **kwargs):
            super(EstanciaForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(
        
                Fieldset( 
                    '<font color = "Black" size=3 face="Comic Sans MS">Datos de estancia </font>',
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
        Cuadricula = forms.CharField(label = "Cuadrícula (*) ", max_length = 100)

        if not edit:
            TipoFardo = forms.ModelChoiceField(TipoFardo.objects.filter(Baja = False), label = "Tipo de Fardos (*)")
            Compra = forms.ModelChoiceField(CompraLote.objects.all().filter(lote = None), label ="Compra del Lote (*)")
        else:
            TipoFardo = forms.ModelChoiceField(TipoFardo.objects.filter(Baja = False), label = "Tipo de Fardos (*)", widget=forms.HiddenInput())
            Compra = forms.ModelChoiceField(CompraLote.objects.all(), label ="Compra del Lote (*)", widget=forms.HiddenInput())

        def __init__(self, *args, **kwargs):
            super(LoteForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(
            
                Fieldset( 
                    '<font color = "Black" size=3 face="Comic Sans MS">Datos de lote </font>',
                    Field('Peso', placeholder="Peso del lote"),
                    Field('Compra'),
                ),
                Fieldset( 
                    '<font color = "Black" size=3 face="Comic Sans MS">Datos de fardos </font>',
                    Field('CantFardos', placeholder="Cantidad de fardos"),
                    Field('TipoFardo', placeholder = "Tipo de fardos"),
                ),
                Fieldset( 
                    '<font color = "Black" size=3 face="Comic Sans MS">Ubicacion </font>',
                    Field('Cuadricula', placeholder="Ubicación del Lote")
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
                raise ValidationError("El peso debe ser 280-300kg por fardo")
            return peso
    
        def save(self, *args, **kwarg):           
            lote = super(LoteForm, self).save(commit=False)
            c = self.cleaned_data['Compra']
            lote.Estancia = c.Estancia
            lote.save()
            

    return LoteForm


# ********************************* Formularios de Fardo *********************************

def FardoFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros
    class FardoForm(ModelForm):
        class Meta:
            model = Fardo
            exclude = ['Baja', 'DetalleOrden', 'Peso']

        e = edit
        if e:
            Lote = forms.ModelChoiceField(Lote.objects.all(), label ="Lote de fardos (*)", widget=forms.HiddenInput())
        else:
            Lote = forms.ModelChoiceField(Lote.disponibles.all(), label ="Lote de fardos (*)")

        CV = forms.FloatField(label ="Coeficiente de variación (*)", min_value = 0)
        AlturaMedia = forms.FloatField(label ="Altura media (*)", min_value = 0)
        Rinde = forms.FloatField(label ="Rinde (*)", min_value = 0)
        Finura = forms.FloatField(label ="Finura (*)", min_value = 0)
        Romana = forms.FloatField(label ="Romana (*)", min_value = 0)

        def __init__(self, *args, **kwargs):
            super(FardoForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            if not self.e:
                self.helper.layout = Layout(
                    Fieldset( 
                        '<font color = "Black" size=3 face="Comic Sans MS">Datos principales </font>',
                        Field('Lote', css_class= ".col-lg-3",placeholder='asd'),
                    ),
                    Fieldset(
                        '<font color = "Black" size=3 face="Comic Sans MS">Especificaciones</font>',
                        Field('Rinde', placeholder="Rinde"),
                        Field('Finura', placeholder="Finura"),
                        Field('CV', placeholder="Coeficiente de variación"),
                        Field('AlturaMedia', placeholder="Altura media"),
                        Field('Romana', placeholder="Romana"),
                    ),

                    HTML('<p>(*)Campos obligatorios.</p>'),
                )
            else:                
                self.helper.layout = Layout(
                    Fieldset(
                        '<font color = "Black" size=3 face="Comic Sans MS">Especificaciones a modificar</font>',
                        Field('Peso', placeholder="Peso"),
                        Field('Rinde', placeholder="Rinde"),
                        Field('Finura', placeholder="Finura"),
                        Field('CV', placeholder="Coeficiente de variación"),
                        Field('AlturaMedia', placeholder="Altura media"),
                        Field('Romana', placeholder="Romana"),
                        Field('Lote', css_class= ".col-lg-3",placeholder='asd'),
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
        Email = forms.CharField(label = "E-mail", required = False)
        Telefono = forms.CharField(label = "Teléfono", required = False)

        class Meta:
            model = Productor
            exclude = ['Baja']

        if not edit:
            DNI = ARDNIField(label="DNI (*)")
            CUIL = ARCUITField(label="CUIL (*)")

        else:   
            DNI = ARDNIField(label="DNI (*)", widget=forms.HiddenInput())
            CUIL = ARCUITField(label="CUIL (*)", widget=forms.HiddenInput())



        def __init__(self, *args, **kwargs):
            super(ProductorForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(

                Fieldset( 
                    '<font color = "Black" size=3 face="Arial">Datos de productor </font>',
                    Field('Nombre', css_class= ".col-lg-3",placeholder='Nombre'),
                    Field('Apellido', placeholder="Apellido"),
                    Field('DNI', placeholder="DNI"),
                    Field('CUIL', placeholder="CUIL XX-XXXXXXXX-X"),
                    Field('Email', placeholder = "E-mail"),
                    Field('Telefono', placeholder = "Teléfono"),
                ),
                HTML('<p>(*)Campos obligatorios.</p>'),
            )

        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submibl', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

    return ProductorForm        

# ********************************* Formularios de Representante *********************************

def RepresentanteFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros

    class RepresentanteForm(forms.ModelForm):
        
        Nombre = forms.CharField(label="Nombre (*)")
        Apellido = forms.CharField(label="Apellido (*)")
        Telefono = forms.CharField(label = "Teléfono", required=False)
        Email = forms.CharField(label = "E-mail", required=False)

        class Meta:
            exclude = ['Baja']
            model = Representante
            widgets = {
           'Zona': forms.Select(choices=[('Sur', 'Sur'), ('Norte', 'Norte')])
            }


        if not edit:
            NroLegajo = forms.IntegerField(label ="Nro. Legajo (*)")
            DNI = ARDNIField(label="DNI (*)")
        else:
            NroLegajo = forms.IntegerField(label ="Nro. Legajo (*)", widget=forms.HiddenInput())
            DNI = ARDNIField(label="DNI (*)",  widget=forms.HiddenInput())
 
        def __init__(self, *args, **kwargs):
            super(RepresentanteForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(

                Fieldset( 
                    '<font color = "Black" size=3 face="Arial">Datos de representante </font>',
                    Field('Nombre', css_class= ".col-lg-3",placeholder='Nombre'),
                    Field('Apellido', placeholder="Apellido"),
                    Field('DNI', placeholder="DNI"),
                    Field('NroLegajo', placeholder="Nro. Legajo"), 
                    Field('Email', placeholder = "E-mail"),
                    Field('Telefono', placeholder = "Teléfono"),
                    Field('Zona', placeholder="Zona"),
                ),
                HTML('<p>(*)Campos obligatorios.</p>'),
            )

        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submit', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

    return RepresentanteForm



#PRODUCCION

# ********************************* Formularios de Orden de Produccion *********************************


def OrdenProduccionFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros

    class OrdenProduccionForm(forms.ModelForm):
        
        e = edit

        class Meta:
            model = OrdenProduccion
            exclude = ['Finalizada',]

        if not e:
            CantRequerida = forms.IntegerField(label = "Cantidad requerida (*)", min_value = 0)
            CV = forms.FloatField(label ="Coeficiente de variación (*)", min_value = 0)
            AlturaMedia = forms.FloatField(label ="Altura media (*)", min_value = 0)
            Finura = forms.FloatField(label ="Finura (*)", min_value = 0)        # Unidad de Medida Micrones
            Romana = forms.FloatField(label ="Romana (*)", min_value = 0)
            Rinde = forms.FloatField(label ="Rinde (*)", min_value = 0)
        else: 
            CantRequerida = forms.IntegerField(label = "Cantidad requerida (*)", min_value = 0, widget=forms.HiddenInput())
            CV = forms.FloatField(label ="Coeficiente de variación (*)", min_value = 0, widget=forms.HiddenInput())
            AlturaMedia = forms.FloatField(label ="Altura media (*)", min_value = 0, widget=forms.HiddenInput())
            Finura = forms.FloatField(label ="Finura (*)", min_value = 0, widget=forms.HiddenInput())        # Unidad de Medida Micrones
            Romana = forms.FloatField(label ="Romana (*)", min_value = 0, widget=forms.HiddenInput())
            Rinde = forms.FloatField(label ="Rinde (*)", min_value = 0, widget=forms.HiddenInput())

        Servicio = forms.ModelChoiceField(Servicio.objects.filter(Transitorio = False), label ="Servicios a Realizar (*)")


        def __init__(self, *args, **kwargs):
            super(OrdenProduccionForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            if not self.e:
                self.helper.layout = Layout(

                    Fieldset( 
                        '<font color = "Black" size=3 face="Comic Sans MS">Datos primarios orden de produccion </font>',
                        Field('CantRequerida', placeholder="Cantidad en kilos requerida"),
                        Field('Servicio', placeholder="Servicio a realizar"),
                    ),
                    Fieldset(
                        '<font color = "Black" size=3 face="Comic Sans MS">Especificaciones orden de produccion</font>',
                        Field('CV', placeholder="Coeficiente de variación"),
                        Field('AlturaMedia', placeholder="Altura media"),
                        Field('Finura', placeholder="Finura"),
                        Field('Romana', placeholder="Romana"),
                        Field('Rinde', placeholder="Rinde")
                    ),
                    HTML('<p>(*)Campos obligatorios.</p>'),
                )
            else:
                self.helper.layout = Layout(

                    Fieldset( 
                            '<font color = "Black" size=3 face="Comic Sans MS">Seleccione nuevo servicio </font>',
                            Field('Servicio', placeholder="Servicios a realizar"),


                            Field('CantRequerida', placeholder="Cantidad en kilos requeridos"),
                            Field('CV', placeholder="Coeficiente de variación"),
                            Field('AlturaMedia', placeholder="Altura media"),
                            Field('Finura', placeholder="Finura"),
                            Field('Romana', placeholder="Romana"),
                            Field('Rinde', placeholder="Rinde")
                        ),
                        HTML('<p>(*)Campos obligatorios.</p>'),
                )
          
        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submit', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

        def save(self, *args, **kwarg):           
            orden = super(OrdenProduccionForm, self).save(commit=False)
            orden.save()
            
            for p in orden.produccion_set.all():
                p.delete()

            servicio = self.cleaned_data['Servicio']
            s = []
            while servicio != None:
                s.append(servicio)
                servicio = servicio.ServicioPrevio

            s.reverse()
            
            for ser in s:
                p = Produccion.objects.create(Orden=orden, Servicio = ser)
                p.save()

    return OrdenProduccionForm


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

def MaquinariaFormFactory(edit=False):  # Crear una funcion para crear una clase y pasarle parametros

    class MaquinariaForm(forms.ModelForm):
        class Meta:
            model = Maquinaria
            exclude = ['Baja']

        if edit:
            NroSerie = forms.IntegerField(label = "Nro. Serie (*)", widget=forms.HiddenInput())
            Descripcion = forms.CharField(label = "Descripción")
            Servicio = forms.ModelChoiceField(Servicio.objects.all(), label = "Servicio (*)", widget=forms.HiddenInput())
        else:
            NroSerie = forms.IntegerField(label = "Nro. Serie (*)")
            Descripcion = forms.CharField(label= "Descripción")
            Servicio = forms.ModelChoiceField(Servicio.objects.all(), label = "Servicio (*)")
                

   
        def __init__(self, *args, **kwargs):
            super(MaquinariaForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-lg-2'
            self.helper.field_class = 'col-lg-8'
            self.helper.layout = Layout(
                Fieldset( 
                    '<font color = "Black" size=3 face="Comic Sans MS">Datos de maquinaria</font>',
                    Field('NroSerie', css_class= ".col-lg-3",placeholder='Nro de serie'),
                    Field('Servicio'),
                    Field('Descripcion', placeholder="Descripción"),
                ),
                
                HTML('<p>(*)Campos obligatorios.</p>'),
            )

        def setup(self, *args, **kwarg):
            self.helper.add_input(Submit('submit', *args, **kwarg))
            self.helper.add_input(Button('cancelar', 'Cancelar', css_class="btn btn-default",onClick = "history.back()"))

    return MaquinariaForm
            
