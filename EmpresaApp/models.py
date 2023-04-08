from django.db import models

# Create your models here.

class Ciudades(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'Ciudades'

    def __str__(self):
        return self.nombre

class Empresas(models.Model):
    NIT = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    ubicacion = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    fechaFundacion = models.DateField()
    email = models.CharField(max_length=100)
    paginaWeb = models.CharField(max_length=500)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'Empresas'

