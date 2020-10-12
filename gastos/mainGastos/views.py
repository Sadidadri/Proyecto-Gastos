from django.shortcuts import render
from .functions import obtenerPerfiles
# Create your views here.

def index(request):
    perfiles = obtenerPerfiles(request.user) 
    return render(request, 'mainGastos/index.html',{'perfiles':perfiles})