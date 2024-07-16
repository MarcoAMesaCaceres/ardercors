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
    titulo = models.CharField(max_length = 100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Imagen',null=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        fila = "Título: " + self.titulo + " - " + " Descripción" + self.descripcion
        return fila
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super() .delete()

class TipoDeProducto(models.Model):
    id_Tipo_de_producto = models.IntegerField(primary_key=True)
    Nombre = models.TextField(null=True)
    Referencia = models.TextField(null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Usuario(models.Model):
    id_Usuario = models.AutoField(primary_key=True)
    Primer_nombre = models.CharField(max_length=100)
    Segundo_nombre = models.CharField(max_length=100, null=True, blank=True)
    Primer_apellido = models.CharField(max_length=100)
    Segundo_apellido = models.CharField(max_length=100, null=True, blank=True)
    Tipo_documento = models.CharField(max_length=100)
    Documento = models.BigIntegerField(unique=True)
    Direccion = models.CharField(max_length=100)
    Telefono = models.BigIntegerField()
    Correo = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.Primer_nombre} {self.Primer_apellido}"
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
    