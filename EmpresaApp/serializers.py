from rest_framework import serializers
from EmpresaApp.models import Empresas, Ciudades

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empresas
        fields=('NIT', 'nombre', 'descripcion', 'ubicacion', 'telefono', 'fechaFundacion', 'email', 'paginaWeb', 'estado')

    class CuidadSerializer(serializers.ModelSerializer):
        class Meta:
            model = Ciudades
            field = ('nombre')