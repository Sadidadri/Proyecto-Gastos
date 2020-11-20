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

    p = obtenerPerfiles(request.user)
    perfiles = None
    if p != None:
        perfiles = formatear_informacion_del_perfil(p)
    return render(request, 'mainGastos/index.html',{'perfiles':perfiles})

#CRUD de categorías
class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre']

def categoria_list(request):
    table = CategoriaTable(Categorias.objects.all().filter(usuario=request.user))

    return render(request, "crud/categoria/listar_categoria.html", {
        "table": table
    })

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

def perfil_list(request):
    table = PerfilTable(Perfiles.objects.all().filter(usuario=request.user))

    return render(request, "crud/perfil/listar_perfil.html", {
        "table": table
    })


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

def gasto_list(request,plk):
    table = GastoTable(Gastos.objects.all().filter(fk_id_perfil=plk))

    return render(request, "crud/gasto/listar_gasto.html", {
        "table": table
    })

def gasto_view(request, pk,plk, template_name='crud/gasto/detalle_gasto.html'):
    gasto = get_object_or_404(Gastos, pk=pk)    
    return render(request, template_name, {'object':gasto})

def gasto_create(request,plk, template_name='crud/gasto/gasto_create_form.html'):
    form = GastoForm(request.POST or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.usuario = request.user
        f.save()
        return redirect('listar_gasto')
    return render(request, template_name, {'form':form})

def gasto_update(request, pk,plk, template_name='crud/gasto/gasto_form.html'):
    gasto= get_object_or_404(Gastos, pk=pk)
    form = GastoForm(request.POST or None, instance=gasto)
    if form.is_valid():
        form.save()
        return redirect('listar_gasto')
    return render(request, template_name, {'form':form})

def gasto_delete(request, pk,plk, template_name='crud/gasto/gasto_confirm_delete.html'):
    gasto= get_object_or_404(Gastos, pk=pk)    
    if request.method=='POST':
        gasto.delete()
        return redirect('listar_gasto')
    return render(request, template_name, {'object':gasto})