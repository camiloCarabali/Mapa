from django.shortcuts import render, redirect
from django.contrib.auth import logout
from EmpresaApp.backends import CustomAuthBackend
from EmpresaApp.models import Empresas, Ciudades2, Usuarios, Sedes


# Create your views here.
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['clave']
        email = request.POST['email']
        Usuarios.objects.create_user(email, username, contraseña)
        return redirect('inicio')
    else:
        return render(request, 'registro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        user = CustomAuthBackend().authenticate(
            request, email=email, contraseña=contraseña)
        print(user)
        if user is not None:
            # auth_login(request, user)
            if user.rol == 'Administrador':
                return redirect('empresa')
            else:
                return redirect('home')
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})


# @login_required
def vistaBase(request):
    return render(request, "base.html")


# @login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')


# @login_required
def vistaInicioU(request):
    empresas = Empresas.objects.all()
    empresa_coords = []
    for empresa in empresas:
        empresa_coords.append((empresa))

    return render(request, "inicioU.html", {"empresas": empresas, "empresa_coords": empresa_coords})


# muestra las empresas que estan en la base de datos registradas
def mostrarEmpresa(request):
    empresas = Empresas.objects.all()
    empresa_coords = []
    for empresa in empresas:
        empresa_coords.append((empresa))

    return render(request, "inicio.html", {"empresas": empresas, "empresa_coords": empresa_coords})


def mostrarSede(request):
    sedes = Sedes.objects.all()
    sede_coords = []
    for sede in sedes:
        sede_coords.append((sede))
    return render(request, "inicioSede.html", {"sedes": sedes, "sede_coords": sede_coords})


# muestra el formulario para crear las empresas
def creacionEmpresa(request):
    return render(request, "create.html")


def creacionSede(request):
    empresas = Empresas.objects.all()
    ciudades = Ciudades2.objects.all()
    return render(request, "createSede.html", {"ciudades": ciudades, "empresas": empresas})


# guarda la informacion del formulario en la base de datos
def crearEmpresa(request):
    NIT = request.POST['NIT']
    nombre = request.POST['nombre']
    mision = request.POST['mision']
    vision = request.POST['vision']
    descripcion = request.POST['descripcion']
    fechaFundacion = request.POST['fecha']
    email = request.POST['email']
    paginaWeb = request.POST['paginaWeb']

    empresa = Empresas.objects.create(NIT=NIT, nombre=nombre, descripcion=descripcion, fechaFundacion=fechaFundacion,
                                      email=email, paginaWeb=paginaWeb, mision=mision, vision=vision)
    return redirect('empresa')


def crearSede(request):
    empresa = request.POST['empresa']
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    direccion = request.POST['direccion']
    municipio = request.POST['municipio']

    ciudad = Ciudades2.objects.get(nombre=municipio)
    principal = Empresas.objects.get(nombre=empresa)

    sede = Sedes.objects.create(empresa=principal, nombre=nombre, telefono=telefono, direccion=direccion,
                                municipio=ciudad)
    return redirect('sede')


# muestra el formulario para actualizar las empresas
def actualizacionEmpresa(request, NIT):
    empresa = Empresas.objects.get(NIT=NIT)
    return render(request, "update.html", {"empresa": empresa})


def actualizacionSede(request, nombre):
    sede = Sedes.objects.get(nombre=nombre)
    empresas = Empresas.objects.all()
    ciudades = Ciudades2.objects.all()
    return render(request, "updateSede.html", {"sede": sede, 'ciudades': ciudades, 'empresas': empresas})


# guarda la informacion del formulario en la base de datos de la empresa a la cual se le ha hecho la actualizacion
def actualizarEmpresa(request, NIT):
    nombre = request.POST['nombre']
    mision = request.POST['mision']
    vision = request.POST['vision']
    descripcion = request.POST['descripcion']
    fechaFundacion = request.POST['fecha']
    email = request.POST['email']
    paginaWeb = request.POST['paginaWeb']

    empresa = Empresas.objects.get(NIT=NIT)
    empresa.nombre = nombre
    empresa.mision = mision
    empresa.vision = vision
    empresa.descripcion = descripcion
    empresa.fechaFundacion = fechaFundacion
    empresa.email = email
    empresa.paginaWeb = paginaWeb
    empresa.save()

    return redirect('empresa')


def actualizarSede(request, nombreSede):
    empresa = request.POST['empresa']
    #nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    direccion = request.POST['direccion']
    municipio = request.POST['municipio']

    ciudad = Ciudades2.objects.get(nombre=municipio)
    principal = Empresas.objects.get(nombre=empresa)

    sede = Sedes.objects.get(sede=nombreSede)
    sede.nombre = nombreSede
    sede.empresa = principal
    sede.telefono = telefono
    sede.direccion = direccion
    sede.municipio = ciudad
    sede.save()

    return redirect('sede')

# inactiva  la empresa que fue escogida por el usuario
def inactivarEmpresa(request, NIT):
    empresa = Empresas.objects.get(NIT=NIT)
    empresa.estado = False
    empresa.save()
    return redirect('empresa')

def inactivarSede(request, nombre):
    sede = Sedes.objects.get(nombre=nombre)
    sede.estado = False
    sede.save()
    return redirect('sede')
