from .models import Perfiles,Gastos
from datetime import datetime

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
