#from django.conf.urls import url
from django.urls import path
from EmpresaApp import views

urlpatterns = [
    path('', views.mostrarEmpresa),
    path('creacionEmpresa/', views.creacionEmpresa),
    path('crearEmpresa/', views.crearEmpresa),
    path('actualizacionEmpresa/<NIT>', views.actualizacionEmpresa),
    path('actualizarEmpresa/<NIT>', views.actualizarEmpresa),
    path('inactivarEmpresa/<NIT>', views.inactivarEmpresa),
]
