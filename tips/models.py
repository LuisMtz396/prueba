from django.db import models
from django.utils import timezone


# Create your models here.

class Recomendacion(models.Model):
    titulo= models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='Recomendaciones')
    descripcion=models.CharField(max_length=80,blank=True)
    creacion= models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    # CLASE INTERNA
    class Meta:
        verbose_name_plural = 'Recomendaciones'

    def __str__(self):
        return self.titulo


class View(models.Model):
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
