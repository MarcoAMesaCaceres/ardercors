from django.db import models


# Create your models here.
from django.db import models

class TipoDePago(models.Model):
    id_de_Pago = models.IntegerField(primary_key=True)
    Efectivo = models.FloatField(null=True)
    Tarjeta = models.FloatField(null=True)
    Transferencia = models.FloatField(null=True)

class Producto(models.Model):
    id_Producto = models.IntegerField(primary_key=True)
    Precio = models.FloatField(null=True)
    Tamaño = models.IntegerField(null=True)
    Color = models.TextField(null=True)

class TipoDeProducto(models.Model):
    id_Tipo_de_producto = models.IntegerField(primary_key=True)
    Nombre = models.TextField(null=True)
    Referencia = models.TextField(null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Usuario(models.Model):
    id_Usuario = models.IntegerField(primary_key=True)
    Primer_nombre = models.TextField(null=True)
    Segundo_nombre = models.TextField(null=True)
    Primer_apellido = models.TextField(null=True)
    Segundo_apellido = models.TextField(null=True)
    Tipo_documento = models.TextField(null=True)
    Documento = models.BigIntegerField(null=True)
    Direccion = models.TextField(null=True)
    Telefono = models.FloatField(null=True)
    Correo = models.TextField(null=True)

class Compra(models.Model):
    id_Compra = models.IntegerField(primary_key=True)
    Cantidad = models.IntegerField(null=True, default=None)
    Valor = models.BigIntegerField(null=True, default=None)
    Fecha = models.DateTimeField(auto_now_add=True)
    tipo_de_pago = models.ForeignKey(TipoDePago, on_delete=models.CASCADE)

class Venta(models.Model):
    id_Venta = models.IntegerField(primary_key=True)
    Fecha = models.DateTimeField(auto_now_add=True)
    Valor = models.FloatField(null=True)
    tipo_de_pago = models.ForeignKey(TipoDePago, on_delete=models.CASCADE)
    
class Material(models.Model):
    id_Material = models.IntegerField(primary_key=True)
    Calidad = models.TextField(null=True)
    Tamaño = models.TextField(null=True)
    Color = models.TextField(null=True)
    Tipo = models.TextField(null=True)
    Nombre = models.TextField(null=True)
    Precio = models.FloatField(null=True)