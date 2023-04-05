from rest_framework import serializers
from EmpresaApp.models import Empresas, Ciudad

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empresas
        fields=('nombre', 'descripcion', 'ubicacion', 'telefono', 'fechaFundacion', 'email', 'paginaWeb')

class CuidadSerializer(serializers.ModelSerializer):

    class Meta:
        model=Ciudad
        field=('nombre')