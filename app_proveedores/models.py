from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    tipo_suministro = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} ({self.tipo_suministro})'
