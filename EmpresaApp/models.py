from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Empresas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    ubicacion = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    fechaFundacion = models.DateField()
    email = models.CharField(max_length=100)
    paginaWeb = models.CharField(max_length=500)





