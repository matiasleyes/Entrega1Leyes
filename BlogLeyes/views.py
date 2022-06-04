from django.shortcuts import render
from .models import *
from django.http import HttpResponse 
from .forms import WriterForm
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
            writers = Writer.objects.filter()
            return render(request, "BlogLeyes/inicio.html")
    else:

        myForm = WriterForm()

    return render(request, "BlogLeyes/writer.html", {"myForm": myForm})

def themes(request):
    return render(request, "BlogLeyes/themes.html")

def topics(request):
    return render(request, "BlogLeyes/topics.html")

def owner(request):
    return render(request, "BlogLeyes/owner.html")

def donor(request):
    return render(request, "BlogLeyes/donor.html")

def articulo(request):
    return render(request, "BlogLeyes/articulo.html")

def writerForm(request):

    if request.method == "POST":

        myForm = WriterForm(request.POST)
        print(myForm)
        if myForm.is_valid:
            information = myForm.cleaned_data
            writer = Writer(nombre = information["nombre"], apellido = information["apellido"], edad = information["edad"], especialidad= information["especialidad"])
            writer.save()
            return render(request, "BlogLeyes/inicio.html")
        else:
            return HttpResponse("estoy en el else del segundo if")
    else:

        myForm = WriterForm()

    return render(request, "BlogLeyes/writerForm.html", {"myForm": myForm})

