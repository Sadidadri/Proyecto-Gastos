from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User,Permission
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from django import forms
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .tables import CategoriaTable,PerfilTable,GastoTable
from .filters import CategoriaFilter,PerfilFilter,GastoFilter
from .models import Categorias,Perfiles,Gastos
from .forms import GastoForm,CategoriaForm,PerfilForm,SignUpForm
from .tokens import account_activation_token
from django.core.mail import send_mail

from .functions import obtenerPerfiles,formatear_informacion_del_perfil,envia_email_confirmacion,obtener_gasto_mas_caro,obtener_gasto_mas_barato

def index(request):
    p = obtenerPerfiles(request.user)
    perfiles = None
    if p != None:
        perfiles = formatear_informacion_del_perfil(p)
    return render(request, 'mainGastos/index.html',{'perfiles':perfiles})

def cuenta_activada(request):
    return render(request, 'registration/account_activation_email_success.html')

#CRUD de categorías
def categoria_list(request):
    table = CategoriaTable(Categorias.objects.all().filter(usuario=request.user))
    mensajeNoCategorias = False
    notTheOwner = False

    if not Categorias.objects.filter(usuario=request.user):
        mensajeNoCategorias = True    
    return render(request, "crud/categoria/listar_categoria.html", {
        "table": table,
        "mensajeNoCategorias":mensajeNoCategorias
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
    isOwner = False
    userOfCategory = Categorias.objects.get(id=pk).usuario
    if (request.user == userOfCategory):
        isOwner = True
    if form.is_valid():
        form.save()
        return redirect('listar_categoria')
    return render(request, template_name, {'form':form,'isOwner':isOwner})

def categoria_delete(request, pk, template_name='crud/categoria/categoria_confirm_delete.html'):
    categoria= get_object_or_404(Categorias, pk=pk)    
    isOwner = False
    userOfCategory = Categorias.objects.get(id=pk).usuario
    if (request.user == userOfCategory):
        isOwner = True
    if request.method=='POST':
        categoria.delete()
        return redirect('listar_categoria')
    return render(request, template_name, {'object':categoria,'isOwner':isOwner})
   

#CRUD de perfiles

def perfil_list(request):
    table = PerfilTable(Perfiles.objects.all().filter(usuario=request.user))
    mensajeNoPerfiles = False
    
    if not Perfiles.objects.filter(usuario=request.user):
        mensajeNoPerfiles = True    
    return render(request, "crud/perfil/listar_perfil.html", {
        "table": table,
        "mensajeNoPerfiles":mensajeNoPerfiles
    })

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
    isOwner = False
    userOfProfile = Perfiles.objects.get(id=pk).usuario
    if (request.user == userOfProfile):
        isOwner = True
    if form.is_valid():
        form.save()
        return redirect('listar_perfil')
    return render(request, template_name, {'form':form,'isOwner':isOwner})

def perfil_delete(request, pk, template_name='crud/perfil/perfil_confirm_delete.html'):
    perfil= get_object_or_404(Perfiles, pk=pk) 
    isOwner = False
    userOfProfile = Perfiles.objects.get(id=pk).usuario
    if (request.user == userOfProfile):
        isOwner = True   
    if request.method=='POST':
        perfil.delete()
        return redirect('listar_perfil')
    return render(request, template_name, {'object':perfil,'isOwner':isOwner})

#CRUD de gastos

def gasto_list(request,plk):
    table = GastoTable(Gastos.objects.all().filter(fk_id_perfil=plk))
    nombre_perfil = Perfiles.objects.get(id=plk)
    mensajeNoGastos = False
    
    if not Gastos.objects.filter(fk_id_perfil=nombre_perfil):
        mensajeNoGastos = True 
    return render(request, "crud/gasto/listar_gasto.html", {
        "table": table,
        "perfilN":plk,
        "nombre_perfil":nombre_perfil,
        "mensajeNoGastos":mensajeNoGastos
    })

def gasto_view(request, pk,plk, template_name='crud/gasto/detalle_gasto.html'):
    gasto = get_object_or_404(Gastos, pk=pk)    
    return render(request, template_name, {'object':gasto})

def gasto_create(request,plk, template_name='crud/gasto/gasto_create_form.html'):
    perfil = Perfiles.objects.get(id=plk)
    user = perfil.usuario
    existenCategorias = False
    categorias = Categorias.objects.filter(usuario=user)
    if(categorias):
        existenCategorias = True
    form = GastoForm(request.POST or None)
    isOwner = False
    if (request.user == user):
        isOwner = True
    if form.is_valid():
        f = form.save(commit=False)
        f.fk_id_categoria = Categorias.objects.get(id=request.POST['categoria'])
        f.fk_id_perfil = perfil
        f.usuario = request.user
        f.save()
        return redirect('listar_gasto', plk)
    return render(request, template_name, {'existenCategorias':existenCategorias,'categorias':categorias,'form':form,'isOwner':isOwner})

def gasto_update(request, pk,plk, template_name='crud/gasto/gasto_form.html'):
    gasto= get_object_or_404(Gastos, pk=pk)
    form = GastoForm(request.POST or None, instance=gasto)
    isOwner = False
    userOfGasto = Gastos.objects.get(id=pk).fk_id_categoria.usuario
    if (request.user == userOfGasto):
        isOwner = True
    if form.is_valid():
        form.save()
        return redirect('listar_gasto', plk)
    return render(request, template_name, {'form':form,'isOwner':isOwner})

def gasto_delete(request, pk,plk, template_name='crud/gasto/gasto_confirm_delete.html'):
    gasto= get_object_or_404(Gastos, pk=pk)  
    isOwner = False
    userOfGasto = Gastos.objects.get(id=pk).fk_id_categoria.usuario
    if (request.user == userOfGasto):
        isOwner = True   
    if request.method=='POST':
        gasto.delete()
        return redirect('listar_gasto', plk)
    return render(request, template_name, {'object':gasto,'isOwner':isOwner})


#Registro de Usuario
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            envia_email_confirmacion(user,current_site,urlsafe_base64_encode(force_bytes(user.pk)),account_activation_token.make_token(user))
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        
        #Añadir permisos de edicion y borrado de perfiles,categorias y gastos
        permisoEditaPerfiles = Permission.objects.get(name='Can change perfiles')
        permisoBorraPerfiles = Permission.objects.get(name='Can delete perfiles')
        permisoEditaCategorias = Permission.objects.get(name='Can change categorias')
        permisoBorraCategorias = Permission.objects.get(name='Can delete categorias')
        permisoEditaGastos = Permission.objects.get(name='Can change gastos')
        permisoBorraGastos = Permission.objects.get(name='Can delete gastos')
        
        user.user_permissions.add(permisoEditaPerfiles)
        user.user_permissions.add(permisoBorraPerfiles)
        user.user_permissions.add(permisoEditaCategorias)
        user.user_permissions.add(permisoBorraCategorias)
        user.user_permissions.add(permisoEditaGastos)
        user.user_permissions.add(permisoBorraGastos)

        user.save()
        login(request, user)
        return redirect('c_activada')
    else:
        return render(request, 'registration/account_activation_invalid.html')

#Resumen de un perfil
def resumen(request,plk):
    perfil = Perfiles.objects.get(id=plk)

    isOwner = False
    userOfProfile = perfil.usuario
    if (request.user == userOfProfile):
        isOwner = True

    informacion = {}
    informacion['nombre_perfil'] = perfil.nombre
    informacion['mas_caro'] = obtener_gasto_mas_caro(perfil)
    informacion['mas_barato'] = obtener_gasto_mas_barato(perfil)
    return render(request, 'mainGastos/resumen.html',{'isOwner':isOwner,'informacion': informacion})
    
    
    #if not Gastos.objects.filter(fk_id_perfil=nombre_perfil):
    #    mensajeNoGastos = True 
    #return render(request, "crud/gasto/listar_gasto.html", {
    #    "table": table,
    #    "perfilN":plk,
    #    "nombre_perfil":nombre_perfil,
    #    "mensajeNoGastos":mensajeNoGastos
    #})