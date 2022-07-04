from django.db import models
import uuid

# Create your models here.
class Writer(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key=True, max_length=100)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    especialidad = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre, self.apellido, self.edad, self.especialidad

class Themes(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key=True, max_length=100)
    tema = models.CharField(max_length=40)
    def __str__(self):
        return self.tema

class Topics(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key=True, max_length=100)
    subtema = models.CharField(max_length=40)
    themes = models.ForeignKey(Themes, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.subtema

class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    shares = models.IntegerField()
    def __str__(self):
        return self.nombre , self.apellido,

class Donor(models.Model):
    entidad = models.CharField(max_length=60)
    donado = models.IntegerField()
    def __str__(self):
        return self.entidad

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    writer = models.CharField(max_length=40)
    def __str__(self):
        return self.titulo, self.cuerpo, self.writer
