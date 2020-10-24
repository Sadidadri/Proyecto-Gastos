from django.shortcuts import render,redirect,get_object_or_404

from .models import Categorias,Perfiles,Gastos
from django.views.generic import ListView, DetailView
from .tables import CategoriaTable,PerfilTable,GastoTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import CategoriaFilter,PerfilFilter,GastoFilter
from django.forms import ModelForm

from .functions import obtenerPerfiles,formatear_informacion_del_perfil
# Create your views here.

def index(request):
    perfiles = formatear_informacion_del_perfil(obtenerPerfiles(request.user))
    return render(request, 'mainGastos/index.html',{'perfiles':perfiles})

#CRUD de categorías
class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre']

class FilteredCategoriaListView(SingleTableMixin, FilterView):
    model = Categorias
    table_class = CategoriaTable
    template_name = 'crud/categoria/listar_categoria.html'

    filterset_class = CategoriaFilter

def categoria_view(request, pk, template_name='crud/categoria/detalle_categoria.html'):
    categoria = get_object_or_404(Categorias, pk=pk)    
    return render(request, template_name, {'object':categoria})

def categoria_create(request, template_name='crud/categoria/categoria_create_form.html'):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.usuario = request.user
        f.save()
        return redirect('listar_categoria')
    return render(request, template_name, {'form':form})

def categoria_update(request, pk, template_name='crud/categoria/categoria_form.html'):
    categoria= get_object_or_404(Categorias, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('listar_categoria')
    return render(request, template_name, {'form':form})

def categoria_delete(request, pk, template_name='crud/categoria/categoria_confirm_delete.html'):
    categoria= get_object_or_404(Categorias, pk=pk)    
    if request.method=='POST':
        categoria.delete()
        return redirect('listar_categoria')
    return render(request, template_name, {'object':categoria})
   

#CRUD de perfiles
class PerfilForm(ModelForm):
    class Meta:
        model = Perfiles
        fields = ['nombre']

class FilteredPerfilListView(SingleTableMixin, FilterView):
    model = Perfiles
    table_class = PerfilTable
    template_name = 'crud/perfil/listar_perfil.html'

    filterset_class = PerfilFilter

def perfil_view(request, pk, template_name='crud/perfil/detalle_perfil.html'):
    perfil = get_object_or_404(Perfiles, pk=pk)    
    return render(request, template_name, {'object':perfil})

def perfil_create(request, template_name='crud/perfil/perfil_create_form.html'):
    form = PerfilForm(request.POST or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.usuario = request.user
        f.save()
        return redirect('listar_perfil')
    return render(request, template_name, {'form':form})

def perfil_update(request, pk, template_name='crud/perfil/perfil_form.html'):
    perfil= get_object_or_404(Perfiles, pk=pk)
    form = PerfilForm(request.POST or None, instance=perfil)
    if form.is_valid():
        form.save()
        return redirect('listar_perfil')
    return render(request, template_name, {'form':form})

def perfil_delete(request, pk, template_name='crud/perfil/perfil_confirm_delete.html'):
    perfil= get_object_or_404(Perfiles, pk=pk)    
    if request.method=='POST':
        perfil.delete()
        return redirect('listar_perfil')
    return render(request, template_name, {'object':perfil})

#CRUD de gastos
class GastoForm(ModelForm):
    class Meta:
        model = Gastos
        fields = ['fk_id_perfil','fk_id_categoria','descripción','precio','fecha']

class FilteredGastoListView(SingleTableMixin, FilterView):
    model = Gastos
    table_class = GastoTable
    template_name = 'crud/gasto/listar_gasto.html'

    filterset_class = GastoFilter

def gasto_view(request, pk, template_name='crud/gasto/detalle_gasto.html'):
    gasto = get_object_or_404(Gastos, pk=pk)    
    return render(request, template_name, {'object':gasto})

def gasto_create(request, template_name='crud/gasto/gasto_create_form.html'):
    form = GastoForm(request.POST or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.usuario = request.user
        f.save()
        return redirect('listar_gasto')
    return render(request, template_name, {'form':form})

def gasto_update(request, pk, template_name='crud/gasto/gasto_form.html'):
    gasto= get_object_or_404(Gastos, pk=pk)
    form = GastoForm(request.POST or None, instance=gasto)
    if form.is_valid():
        form.save()
        return redirect('listar_gasto')
    return render(request, template_name, {'form':form})

def gasto_delete(request, pk, template_name='crud/gasto/gasto_confirm_delete.html'):
    gasto= get_object_or_404(Gastos, pk=pk)    
    if request.method=='POST':
        gasto.delete()
        return redirect('listar_gasto')
    return render(request, template_name, {'object':gasto})