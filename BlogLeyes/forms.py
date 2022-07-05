from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField(label="Modificar Apellido")
    first_name = forms.CharField(label="Modificar Nombre")

    class Meta: 
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts={k:"" for k in fields} 


class WriterForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    especialidad = forms.CharField(max_length=50)

class ThemesForm(forms.Form):
    tema = forms.CharField(max_length=40)


class TopicsForm(forms.Form):
    subtema = forms.CharField(max_length=40)

class OwnerForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    shares = forms.IntegerField()


class DonorForm(forms.Form):
    entidad = forms.CharField(max_length=60)
    donado = forms.IntegerField()


class articuloForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=1000)
