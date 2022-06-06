from django.shortcuts import render
from .models import *
from django.http import HttpResponse 
from .forms import WriterForm, ThemesForm, OwnerForm, DonorForm
# Create your views here.

def inicio(request):

    return render(request, "BlogLeyes/inicio.html")

def writer(request):
    if request.method == "POST":

        myForm = WriterForm(request.POST)
        print(myForm)
        if myForm.is_valid:
            information = myForm.cleaned_data
            writer = Writer(nombre = information["nombre"], apellido = information["apellido"], edad = information["edad"], especialidad= information["especialidad"])
            writer.save()
            return render(request, "BlogLeyes/inicio.html")
    else:

        myForm = WriterForm()

    return render(request, "BlogLeyes/writer.html", {"myForm": myForm})

def themes(request):
    temas = Themes.objects.all() 
    if request.method == "POST":

        myForm = ThemesForm(request.POST)
        print(myForm)
        if myForm.is_valid:
            information = myForm.cleaned_data
            theme = Themes(tema = information["tema"])
            theme.save()
            return render(request, "BlogLeyes/inicio.html")
    else:

        myForm = ThemesForm()

    return render(request, "BlogLeyes/themes.html", {"myForm": myForm})



def topics(request):
    return render(request, "BlogLeyes/topics.html")

def owner(request):
    if request.method == "POST":

        myForm = OwnerForm(request.POST)
        print(myForm)
        if myForm.is_valid:
            information = myForm.cleaned_data
            owners = Owner(nombre = information["nombre"], apellido = information["apellido"], shares = information["shares"])
            owners.save()
            owners = Owner.objects.filter()
            return render(request, "BlogLeyes/inicio.html")
    else:

        myForm = OwnerForm()

    return render(request, "BlogLeyes/owner.html", {"myForm": myForm})

def donor(request):
    if request.method == "POST":

        myForm = DonorForm(request.POST)
        print(myForm)
        if myForm.is_valid:
            information = myForm.cleaned_data
            donor = Donor(entidad = information["entidad"], donado = information["donado"])
            donor.save()
            return render(request, "BlogLeyes/inicio.html")
    else:

        myForm = DonorForm()

    return render(request, "BlogLeyes/donor.html", {"myForm": myForm})

def articulo(request):
    return render(request, "BlogLeyes/articulo.html")

def busquedaEscritor(request):
    return render(request, 'BlogLeyes/busquedaEscritor.html')


def buscar(request):
    if request.GET['apellido']:
        apellido = request.GET['apellido']
        escritor = Writer.objects.filter(apellido=apellido)
        return render(request, 'BlogLeyes/resultadosBusqueda.html', {'escritor': escritor, 'apellido':apellido})
    else:
        respuesta = "No se ingresó ningun escritor"
        return HttpResponse(respuesta)

