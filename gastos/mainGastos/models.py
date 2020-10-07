from django.db import models
from django.conf import settings

# Create your models here.

class Categorias(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nombre = models.CharField(max_length=150)

class Perfiles(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nombre = models.CharField(max_length=150)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    
class Gastos(models.Model):
    fk_id_categoria = models.ForeignKey(Categorias,on_delete=models.SET_NULL,null = True)
    fk_id_perfil = models.ForeignKey(Perfiles,on_delete=models.SET_NULL, null = True)
    descripción = models.CharField(max_length=200,null=True,blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateField()