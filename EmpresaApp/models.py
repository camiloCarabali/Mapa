from djongo import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import check_password
# Create your models here.

class Ciudades2(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'Ciudades'

    def __str__(self):
        return self.nombre

class Empresas(models.Model):
    NIT = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    ubicacion = models.ForeignKey(Ciudades2, on_delete=models.CASCADE) #DIRECCIÓN
    telefono = models.CharField(max_length=100)
    fechaFundacion = models.DateField()
    email = models.CharField(max_length=100)
    paginaWeb = models.CharField(max_length=500)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'Empresas'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, contraseña, **extra_fields):
        if not email:
            raise ValueError('El correo electronico debe ser ingresado')
        if not username:
            raise ValueError('El nombre de usuario debe ser ingresado')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            rol='Cliente',
            contraseña=contraseña,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, contraseña, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        user = self.create_user(
            username=username,
            email=email,
            contraseña=contraseña,
        )
        user.rol = 'Administrador'
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuarios(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    contraseña = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    PASSWORD_FIELD = 'contraseña'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
    last_login = None
    password = None

    class Meta:
        db_table = 'Usuarios'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.rol == 'Administrador'

    @property
    def is_cliente(self):
        return self.rol == 'Cliente'

    def check_password(self, raw_password):
        if raw_password == self.contraseña:
            return True
        return False
