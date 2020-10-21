from django.contrib import admin
from .models import Perfiles,Categorias,Gastos
# Register your models here.

class PerfilesAdmin(admin.ModelAdmin):
    list_display = ["usuario","nombre","fecha_de_creacion"]
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ["usuario","nombre"]
class GastosAdmin(admin.ModelAdmin):
    list_display = ["fk_id_categoria","fk_id_perfil","descripción","precio","fecha"]

admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Perfiles,PerfilesAdmin)
admin.site.register(Gastos,GastosAdmin)