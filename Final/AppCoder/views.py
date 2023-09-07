from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, "AppCoder/login.html")


def crear_usuarios(request):
    return render(request, "AppCoder/usuarioFormulario.html")