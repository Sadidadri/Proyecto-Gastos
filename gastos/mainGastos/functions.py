from .models import Perfiles

def obtenerPerfiles(user):
    if Perfiles.objects.filter(usuario = user):
        return Perfiles.objects.filter(usuario = user)
    return None