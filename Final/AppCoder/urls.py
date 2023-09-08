
from django.urls import path
from .views import *

urlpatterns = [

   
    path('', login),
    path('crear_usuarios/', crear_usuarios, name="crear_usuarios"),

    
]
