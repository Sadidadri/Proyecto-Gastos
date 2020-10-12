from django.contrib import admin
from .models import Perfiles,Categorias
# Register your models here.

class PerfilesAdmin(admin.ModelAdmin):
    list_display = ["usuario","nombre","fecha_de_creacion"]
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ["usuario","nombre"]

admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Perfiles,PerfilesAdmin)
