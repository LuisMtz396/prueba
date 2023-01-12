from django.db import models
from django.utils import timezone


# Create your models here.

class Vacante(models.Model):
    nombre_empresa= models.CharField(max_length=50)
    giro_empresarial= models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='vacantes')
    creacion= models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    # CLASE INTERNA
    class Meta:
        verbose_name = 'Vacantes'
        verbose_name_plural = 'vacantes y bolsa de trabajo'

    def __str__(self):
        return self.nombre_empresa


class View(models.Model):
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
