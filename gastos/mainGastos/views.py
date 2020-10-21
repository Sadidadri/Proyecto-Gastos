from django.shortcuts import render

from .models import Categorias,Perfiles,Gastos
from django.views.generic import ListView, DetailView
from .tables import CategoriaTable,PerfilTable,GastoTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import CategoriaFilter,PerfilFilter,GastoFilter

from .functions import obtenerPerfiles,formatear_informacion_del_perfil
# Create your views here.

def index(request):
    perfiles = formatear_informacion_del_perfil(obtenerPerfiles(request.user))
    #raise Exception("stop")
    #raise Exception(str(perfiles["Gastos De Casa"]))
    return render(request, 'mainGastos/index.html',{'perfiles':perfiles})

#CRUD de categorías

class FilteredCategoriaListView(SingleTableMixin, FilterView):
    model = Categorias
    table_class = CategoriaTable
    template_name = 'crud/categoria/listar_categoria.html'

    filterset_class = CategoriaFilter

#CRUD de perfiles

class FilteredPerfilListView(SingleTableMixin, FilterView):
    model = Perfiles
    table_class = PerfilTable
    template_name = 'crud/perfil/listar_perfil.html'

    filterset_class = PerfilFilter

#CRUD de gastos

class FilteredGastoListView(SingleTableMixin, FilterView):
    model = Gastos
    table_class = GastoTable
    template_name = 'crud/gasto/listar_gasto.html'

    filterset_class = GastoFilter