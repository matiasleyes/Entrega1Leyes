from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("vistsa inicio")

def writer(request):
    return HttpResponse("vistsa writer")

def themes(request):
    return HttpResponse("vistsa themes")

def topics(request):
    return HttpResponse("vistsa topics")

def owner(request):
    return HttpResponse("vistsa owner")

def donor(request):
    return HttpResponse("vistsa donor")

def articulo(request):
    return HttpResponse("vistsa articulo")