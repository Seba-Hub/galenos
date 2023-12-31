from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)


    def __str__(self):
        return self.nombre