from django.shortcuts import render, redirect
from django.contrib.auth import logout
from EmpresaApp.backends import CustomAuthBackend
from EmpresaApp.models import Empresas, Ciudades2, Usuarios

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

#muestra las empresas que estan en la base de datos registradas
def mostrarEmpresa(request):
    empresas = Empresas.objects.all()
    empresa_coords = []
    for empresa in empresas:
        empresa_coords.append((empresa))

    return render(request, "inicio.html", {"empresas": empresas, "empresa_coords": empresa_coords})

#muestra el formulario para crear las empresas 
def creacionEmpresa(request):
    ciudades = Ciudades2.objects.all()
    return render(request, "create.html", {"ciudades": ciudades})

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

    ciudad = Ciudades2.objects.get(nombre=ubicacion)
    print("Ciudad:",ciudad.pk)
    empresa = Empresas.objects.create(NIT=NIT, nombre=nombre, descripcion=descripcion, ubicacion=ciudad, telefono=telefono,
                                      fechaFundacion=fechaFundacion, email=email, paginaWeb=paginaWeb)
    return redirect('empresa')

#muestra el formulario para actualizar las empresas 
def actualizacionEmpresa(request, NIT):
    empresa = Empresas.objects.get(NIT=NIT)
    ciudades = Ciudades2.objects.all()
    return render(request, "update.html", {"empresa": empresa, 'ciudades': ciudades})

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

    ciudad = Ciudades2.objects.get(nombre=ubicacion)

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

    return redirect('empresa')

#inactiva  la empresa que fue escogida por el usuario
def inactivarEmpresa(request, NIT):
    empresa = Empresas.objects.get(NIT=NIT)
    empresa.estado = False
    empresa.save()
    return redirect('empresa')
