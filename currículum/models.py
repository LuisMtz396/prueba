from django.db import models
from .choices import carreras
from .choices import posgrados
# Create your models here.
class Egresado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    edad=models.IntegerField()
    correo_institucional = models.EmailField()
    generacion = models.CharField(max_length=9)
    telefono = models.CharField(max_length=10)
    cv = models.FileField(upload_to='curriculum')
    carrera = models.CharField(max_length=32, choices=carreras, default='IGE')
    posgrado=models.CharField(max_length=2,choices=posgrados,default='Si',verbose_name = "¿Estudia o cuenta con un posgrado?")
    tipo_posgrado=models.CharField(max_length=80,blank=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)
  
     # CLASE INTERNA

    def __str__(self):
        return self.nombre
    