from django import forms

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
