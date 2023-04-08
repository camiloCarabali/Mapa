from datetime import datetime
import random
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmpresaApp.models import Empresas, Ciudades
from EmpresaApp.serializers import EmpresaSerializer


# Create your views here.
#muestra las empresas que estan en la base de datos registradas
def mostrarEmpresa(request):
    empresas = Empresas.objects.all()
    empresa_coords = []
    for empresa in empresas:
       empresa_coords.append((empresa))
      
    return render(request, "inicio.html", {"empresas": empresas, "empresa_coords": empresa_coords})
#muestra el formulario para crear las empresas 
def creacionEmpresa(request):
    ciudades = Ciudades.objects.all()
    return render(request, "creacionEmpresa.html", {"ciudades": ciudades})

#guarda la informacion del formulario en la base de datos
def crearEmpresa(request):
    NIT = request.POST['NIT']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    ubicacion = request.POST['ubicacion']
    telefono = request.POST['telefono']
    fechaFundacion = request.POST['fecha']
    email = request.POST['email']
    paginaWeb = request.POST['paginaWeb']

    ciudad = Ciudades.objects.get(nombre=ubicacion)

    empresa = Empresas.objects.create(NIT=NIT, nombre=nombre, descripcion=descripcion, ubicacion=ciudad, telefono=telefono,
                                      fechaFundacion=fechaFundacion, email=email, paginaWeb=paginaWeb)
    return redirect('/')

#muestra el formulario para actualizar las empresas 
def actualizacionEmpresa(request, NIT):
    empresa = Empresas.objects.get(NIT=NIT)
    ciudades = Ciudades.objects.all()
    return render(request, "actualizacionEmpresa.html", {"empresa": empresa, 'ciudades': ciudades})

#guarda la informacion del formulario en la base de datos de la empresa a la cual se le ha hecho la actualizacion
def actualizarEmpresa(request, NIT):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    ubicacion = request.POST['ubicacion']
    telefono = request.POST['telefono']
    fechaFundacion = request.POST['fecha']
    email = request.POST['email']
    paginaWeb = request.POST['paginaWeb']

    print(ubicacion)

    ciudad = Ciudades.objects.get(nombre=ubicacion)

    print(ciudad)

    empresa = Empresas.objects.get(NIT=NIT)
    empresa.nombre = nombre
    empresa.descripcion = descripcion
    empresa.ubicacion = ciudad
    empresa.telefono = telefono
    empresa.fechaFundacion = fechaFundacion
    empresa.email = email
    empresa.paginaWeb = paginaWeb
    empresa.save()

    return redirect('/')

#inactiva  la empresa que fue escogida por el usuario
def inactivarEmpresa(request, NIT):
    empresa = Empresas.objects.get(NIT=NIT)
    empresa.estado = False
    empresa.save()
    return redirect('/')