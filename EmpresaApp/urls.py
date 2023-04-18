#from django.conf.urls import url
from django.urls import path
from EmpresaApp import views

urlpatterns = [
    path('', views.vistaBase, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.vistaInicioU, name='home'),
    path('empresa/', views.mostrarEmpresa, name='empresa'),
    path('creacionEmpresa/', views.creacionEmpresa, name='crear'),
    path('crearEmpresa/', views.crearEmpresa),
    path('actualizacionEmpresa/<NIT>', views.actualizacionEmpresa),
    path('actualizarEmpresa/<NIT>', views.actualizarEmpresa),
    path('inactivarEmpresa/<NIT>', views.inactivarEmpresa),
    path('sede/', views.mostrarSede, name='sede'),
    path('creacionSede/', views.creacionSede, name='crearsede'),
    path('crearSede/', views.crearSede),
    path('actualizacionSede/<nombre>', views.actualizacionSede),
    path('actualizarSede/<nombre>', views.actualizarSede),
    path('inactivarSede/<nombre>', views.inactivarSede),
]
