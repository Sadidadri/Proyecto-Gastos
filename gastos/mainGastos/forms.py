from .models import User,Categorias,Perfiles,Gastos
from django.contrib.auth.forms import UserCreationForm
from django import forms

class GastoForm(forms.ModelForm):
    
    class Meta:
        model = Gastos
        fields = ['descripción','precio','fecha']
        widgets = {
            'descripción': forms.TextInput(attrs={'class':'form-control','placeholder':'Breve descripción del gasto'}),
            'precio': forms.NumberInput(attrs={'class':'form-control','placeholder':'Precio en euros, e.g: 24.99€'}),
            'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Elija una fecha', 'type':'date'}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre para el perfil. e.g Gastos de Oficina'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre para la categoría. e.g Compra en Amazon'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Introduzca una cuenta de correo válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )