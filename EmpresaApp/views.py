from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmpresaApp.models import Empresas
from EmpresaApp.serializers import EmpresaSerializer


# Create your views here.
def mostrarEmpresa(request):
    empresas = Empresas.objects.all()
    return render(request, "inicio.html", {"empresas": empresas})


def creacionEmpresa(request):
    return render(request, "creacionEmpresa.html")


def crearEmpresa(request):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    ubicacion = request.POST['ubicacion']
    telefono = request.POST['telefono']
    fechaFundacion = request.POST['fecha']
    email = request.POST['email']
    paginaWeb = request.POST['paginaWeb']

    empresa = Empresas.objects.create(nombre=nombre, descripcion=descripcion, ubicacion=ubicacion, telefono=telefono,
                                      fechaFundacion=fechaFundacion, email=email, paginaWeb=paginaWeb)
    return redirect('/')


def actualizacionEmpresa(request, id):
    empresa = Empresas.objects.get(id=id)
    return render(request, "actualizacionEmpresa.html", {"empresa": empresa})


def actualizarEmpresa(request, id):
    print(id)
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