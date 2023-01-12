from django.db import models

# Create your models here.


class Registro(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    mensaje = models.TextField(verbose_name='asunto',)
 
     # CLASE INTERNA
    class Meta:
        
        verbose_name_plural = 'Registro Mensajes'

    def __str__(self):
        return self.nombre
