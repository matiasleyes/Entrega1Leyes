from django.shortcuts import render
from .models import *
from django.http import HttpResponse 
from .forms import WriterForm, ThemesForm, OwnerForm, DonorForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def inicio(request):

    return render(request, "BlogLeyes/inicio.html")

#LOGIN-----------------------------------------------------------------------------------------------------------------------------------
def login_request(request):

    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)

                return render(request, "BlogLeyes/inicio.html", {"mensaje":f"bienvenido {username}"})
            else:
                return render(request, "BlogLeyes/inicio.html", {"mensaje":"error, datos incorrectos"})

        else:
            return render(request, "BlogLeyes/errorLogin.html", {"mensaje":"error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "BlogLeyes/login.html", {'form':form}) 


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()

            return render(request, "BlogLeyes/inicio.html", {'mensaje':f'usuario {username} creado'})
    
        else:
            return render(request, "BlogLeyes/inicio.html", {'mensaje':f'no se pudo crea el usuario {username}'})

    else:
        form = UserCreationForm()

        return render(request, "BlogLeyes/register.html", {"form":form})




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

