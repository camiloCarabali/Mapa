#from django.conf.urls import url
from django.urls import path
from EmpresaApp import views

urlpatterns = [
    path('', views.mostrarEmpresa),
    path('creacionEmpresa/', views.creacionEmpresa),
    path('crearEmpresa/', views.crearEmpresa),
    path('actualizacionEmpresa/<id>', views.actualizacionEmpresa),
    path('actualizarEmpresa/<id>', views.actualizarEmpresa),
    path('eliminarEmpresa/<id>', views.eliminarEmpresa),
]
