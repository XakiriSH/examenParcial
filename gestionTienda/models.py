from django.db import models

class Tienda(models.Model):
    direccion = models.CharField(max_length=255)
    provincia = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    telefono_contacto = models.CharField(max_length=20)

class Producto(models.Model):
    descripcion = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    tienda_relacionada = models.ForeignKey(Tienda, on_delete=models.SET_NULL, null=True, blank=True)
