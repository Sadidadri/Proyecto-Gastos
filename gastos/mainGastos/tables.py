import django_tables2 as tables
from .models import Categorias,Gastos,Perfiles

class CategoriaTable(tables.Table):
    class Meta:
       model = Categorias
       template_name = "django_tables2/bootstrap.html"
       fields = ("id","nombre",)

class PerfilTable(tables.Table):
    class Meta:
       model = Perfiles
       template_name = "django_tables2/bootstrap.html"
       fields = ("id","nombre","fecha_de_creacion",)

class GastoTable(tables.Table):
    class Meta:
       model = Gastos
       template_name = "django_tables2/bootstrap.html"
       fields = ("id","fk_id_categoria","fk_id_perfil","descripción","precio","fecha")