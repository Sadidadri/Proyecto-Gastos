from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Categorias(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Perfiles(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nombre = models.CharField(max_length=150)
    fecha_de_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Gastos(models.Model):
    fk_id_categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE,null = True)
    fk_id_perfil = models.ForeignKey(Perfiles,on_delete=models.CASCADE, null = True)
    descripción = models.CharField(max_length=200,null=True,blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        if( self.descripción == None):
            return "Gasto sin descripción ("+str(self.precio)+"€)"
        return self.descripción+" ("+str(self.precio)+"€)"