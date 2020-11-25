import django_tables2 as tables
from .models import Categorias,Gastos,Perfiles
from datetime import datetime
from django.utils.html import format_html

class CategoriaTable(tables.Table):
    class Meta:
       model = Categorias
       template_name = "django_tables2/bootstrap.html"
       fields = ("id","nombre",)

class PerfilTable(tables.Table):
    fecha_de_creacion = tables.Column()

    class Meta:
       model = Perfiles
       template_name = "django_tables2/bootstrap.html"
       fields = ("id","nombre","fecha_de_creacion",)

    def render_fecha_de_creacion(self, value, record):
        value = value.strftime('%d/%m/%Y')
        return format_html("{}", value)

class GastoTable(tables.Table):
    fk_id_categoria = tables.Column(verbose_name= 'Categoría' )
    fecha = tables.Column()
    class Meta:
       model = Gastos
       template_name = "django_tables2/bootstrap.html"
       fields = ("id","fk_id_categoria","descripción","precio","fecha")

    def render_fecha(self, value, record):
        value = value.strftime('%d/%m/%Y')
        return format_html("{}", value)