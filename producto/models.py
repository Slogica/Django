# producto/models.py
from django.db import models

class Producto(models.Model):
    """
    Modelo de datos para los productos de la tienda.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    disponibilidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
