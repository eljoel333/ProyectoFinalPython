from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField();

class Mensaje(models.Model):
    emisor = models.CharField(max_length=30)
    receptor = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=100)
    leido = models.BooleanField()
