from django.shortcuts import render
from .models import *
from django.http import HttpResponse 
from .forms import WriterForm, ThemesForm, OwnerForm, DonorForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


#WRITER---------------------------------------------------------------------------------
def writer(request):
    return render(request,"BlogLeyes/writer.html")

class writerList(ListView):

    model = Writer
    template_name = "BlogLeyes/writerList.html"

class writerDetail(DetailView):

    model = Writer
    template_name = "BlogLeyes/writerDetail.html"

class writerMake(CreateView):

    model = Writer
    success_url = reverse_lazy('writerList')
    fields = [ 'nombre', 'apellido', 'edad','especialidad' ]

class writerUpdate(UpdateView):

    model = Writer
    success_url = reverse_lazy('writerList')
    fields = [ 'nombre', 'apellido', 'edad', 'especialidad' ]

class writerDelete(DeleteView):

    model = Writer
    success_url = reverse_lazy('writerList')

#THEMES---------------------------------------------------------------------------------
def themes(request):
    return render(request,"BlogLeyes/themes.html")

class themesList(ListView):

    model = Themes
    template_name = "BlogLeyes/themesList.html"

class themesDetail(DetailView):

    model = Themes
    template_name = "BlogLeyes/themesDetail.html"

class themesMake(CreateView):

    model = Themes
    success_url = reverse_lazy('themesList')
    fields = [ 'tema' ]

class themesUpdate(UpdateView):

    model = Themes
    success_url = reverse_lazy('themesList')
    fields = [ 'tema' ]

class themesDelete(DeleteView):

    model = Themes
    success_url = reverse_lazy('themesList')


#TOPICS---------------------------------------------------------------------------------
def topics(request):
    return render(request,"BlogLeyes/topics.html")

#OWNER ---------------------------------------------------------------------------------
def owner(request):
    return render(request,"BlogLeyes/owner.html")

class ownerList(ListView):

    model = Owner
    template_name = "BlogLeyes/ownerList.html"

class ownerDetail(DetailView):

    model = Owner
    template_name = "BlogLeyes/ownerDetail.html"

class ownerMake(CreateView):

    model = Owner
    success_url = reverse_lazy('ownerList')
    fields = [ 'nombre', 'apellido', 'shares']

class ownerUpdate(UpdateView):

    model = Owner
    success_url = reverse_lazy('ownerList')
    fields = [ 'nombre', 'apellido', 'shares']

class ownerDelete(DeleteView):

    model = Owner
    success_url = reverse_lazy('ownerList')

#Donor ---------------------------------------------------------------------------------
def donor(request):
    return render(request,"BlogLeyes/donor.html")

class donorList(ListView):

    model = Donor
    template_name = "BlogLeyes/donorList.html"

class donorDetail(DetailView):

    model = Donor
    template_name = "BlogLeyes/donorDetail.html"

class donorMake(CreateView):

    model = Donor
    success_url = reverse_lazy('donorList')
    fields = [ 'entidad', 'donado' ]

class donorUpdate(UpdateView):

    model = Donor
    success_url = reverse_lazy('donorList')
    fields = [ 'entidad', 'donado' ]

class donorDelete(DeleteView):

    model = Donor
    success_url = reverse_lazy('donorList')

#Articulo---------------------------------------------------------------------------------
def articulo(request):
    return render(request, "BlogLeyes/articulo.html")

class articuloList(ListView):

    model = Articulo
    template_name = "BlogLeyes/articuloList.html"

class articuloDetail(DetailView):

    model = Articulo
    template_name = "BlogLeyes/articuloDetail.html"

class articuloMake(CreateView):

    model = Articulo
    success_url = reverse_lazy('articuloList')
    fields = [ 'titulo', 'cuerpo', 'writer' ]

class articuloUpdate(UpdateView):

    model = Articulo
    success_url = reverse_lazy('articuloList')
    fields = [ 'titulo', 'cuerpo', 'writer' ]

class articuloDelete(DeleteView):

    model = Articulo
    success_url = reverse_lazy('articuloList')


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

def aboutus(request):
    return render(request, 'BlogLeyes/Aboutus.html')