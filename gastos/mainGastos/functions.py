from .models import Perfiles,Gastos
from gastos.settings import EMAIL_HOST_USER
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import send_mail
from django.db.models import Max,Min

def obtenerPerfiles(user):
    if user.id == None:
        # user is anon user
        return None
    if Perfiles.objects.filter(usuario = user):
        return Perfiles.objects.filter(usuario = user)
    return None

def formatear_informacion_del_perfil(perfiles):
    diccionario_perfiles = {}    
    for perfil in perfiles:
        g = obtener_gasto_total_y_mensual(perfil)
        gasto_mensual = g[0]
        total_gastos = g[1]
        p_id = perfil.id
        p_nombre = perfil.nombre
        try:
            ultimo_gasto = Gastos.objects.filter(fk_id_perfil=perfil).last()
            cat = str(ultimo_gasto.fk_id_categoria)
            precio = str(ultimo_gasto.precio)
            fecha = str(ultimo_gasto.fecha)
        except:
            #Ocurre cuando se ha creado nuevo perfil y no tiene gasto registrado
            cat = ""
            precio = ""
            fecha = ""
        entrada_diccionario_perfil = {"id":p_id,"fecha_de_creacion":str(perfil.fecha_de_creacion),"categoria":cat,"precio":precio,"fecha":fecha,"gasto_mensual":gasto_mensual,"total_gastos":total_gastos}
        diccionario_perfiles[p_nombre] = entrada_diccionario_perfil
    return diccionario_perfiles

def obtener_gasto_total_y_mensual(perfil):

    mesActual = obtenerMes()
    agnoActual = obtenerAgno()
    gastos = Gastos.objects.filter(fk_id_perfil=perfil)
    gasto_total = 0
    gasto_mensual = 0
    for gasto in gastos:
        gasto_total += gasto.precio
        g_mes = gasto.fecha.strftime("%m")
        g_agno = gasto.fecha.strftime("%Y")
        if g_mes == mesActual and g_agno == agnoActual:
            gasto_mensual += gasto.precio

    return [str(gasto_mensual),str(gasto_total)]

def obtenerMes():
    return datetime.today().strftime("%m")

def obtenerAgno():
    return datetime.today().strftime("%Y")


def envia_email_confirmacion(user,domain,uid,token):
    subject = 'Confirmación de nuevo usuario. Aplicación Gastos'
    
    #send_mail(subject, 'hola', EMAIL_HOST_USER, [user.email], fail_silently = False)
    template = get_template('registration/account_activation_email.html')
    
    content = template.render({
        'user': user,
        'domain': domain,
        'uid': uid,
        'token': token,
    })
    message = EmailMultiAlternatives(subject,'',EMAIL_HOST_USER,[user.email])
    
    message.attach_alternative(content, 'text/html')
    message.content_subtype = "html"
    message.send()

def obtener_gasto_mas_caro(perfil):
    gasto = Gastos.objects.filter(fk_id_perfil=perfil)
    g = gasto.aggregate(Max('precio'))
    max_gasto = Gastos.objects.filter(precio=g['precio__max'] , fk_id_perfil=perfil)[0]
    return str(max_gasto)

def obtener_gasto_mas_barato(perfil):
    gasto = Gastos.objects.filter(fk_id_perfil=perfil)
    g = gasto.aggregate(Min('precio'))
    pr = g['precio__min']
    min_gasto = Gastos.objects.filter(precio=pr , fk_id_perfil=perfil)[0]
    return min_gasto