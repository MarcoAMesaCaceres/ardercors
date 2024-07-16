from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Producto, Material, TipoDePago, Compra, Venta

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)   

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Primer_nombre', 'Segundo_nombre', 'Primer_apellido', 'Segundo_apellido', 
                'Tipo_documento', 'Documento', 'Direccion', 'Telefono', 'Correo']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Precio', 'Tamaño', 'Color', 'titulo', 'imagen', 'descripcion', 'nombre', 'precio']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['Calidad', 'Tamaño', 'Color', 'Tipo', 'Nombre', 'Precio']

class TipoDePagoForm(forms.ModelForm):
    class Meta:
        model = TipoDePago
        fields = ['Efectivo', 'Tarjeta', 'Transferencia']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['Cantidad', 'Valor', 'tipo_de_pago']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['Valor', 'tipo_de_pago']