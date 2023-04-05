from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from datetime import datetime

from EmpresaApp.models import Empresas, Ciudad
from EmpresaApp.serializers import EmpresaSerializer


# Create your views here.
def mostrarEmpresa(request):
    empresas = Empresas.objects.all()
    return render(request, "inicio.html", {"empresas": empresas})


def creacionEmpresa(request):
    ciudades = Ciudad.objects.all()
    return render(request, "creacionEmpresa.html", {"ciudades": ciudades})


def crearEmpresa(request):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    ubicacion = request.POST['ubicacion']
    telefono = request.POST['telefono']
    fechaFundacion = request.POST['fecha']
    email = request.POST['email']
    paginaWeb = request.POST['paginaWeb']

    ciudad = Ciudad.objects.get(nombre=ubicacion)

    empresa = Empresas.objects.create(nombre=nombre, descripcion=descripcion, ubicacion=ciudad, telefono=telefono,
                                      fechaFundacion=fechaFundacion, email=email, paginaWeb=paginaWeb)
    return redirect('/')


def actualizacionEmpresa(request, id):
    empresa = Empresas.objects.get(id=id)
    ciudades = Ciudad.objects.all()
    return render(request, "actualizacionEmpresa.html", {"empresa": empresa, 'ciudades': ciudades})


def actualizarEmpresa(request, id):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    ubicacion = request.POST['ubicacion']
    telefono = request.POST['telefono']
    fechaFundacion = request.POST['fecha']
    email = request.POST['email']
    paginaWeb = request.POST['paginaWeb']

    empresa = Empresas.objects.get(id=id)
    empresa.nombre = nombre
    empresa.descripcion = descripcion
    empresa.ubicacion = ubicacion
    empresa.telefono = telefono
    empresa.fechaFundacion = fechaFundacion
    empresa.email = email
    empresa.paginaWeb = paginaWeb
    empresa.save()

    return redirect('/')


def eliminarEmpresa(request, id):
    empresa = Empresas.objects.get(id=id)
    empresa.delete()
    return redirect('/')


def mostrarCiudad(request):
    ciudades = Ciudad.objects.all()
    return render(request, "actualizacionEmpresa.html", {"ciudades": ciudades})