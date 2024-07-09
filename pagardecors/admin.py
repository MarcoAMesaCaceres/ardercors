from django.contrib import admin
from .models import TipoDePago, Producto, TipoDeProducto, Usuario, Compra, Venta, Material  
# Register your models here.

from django.contrib import admin
from .models import TipoDePago, Producto, TipoDeProducto, Usuario, Compra, Venta, Material

# Register your models here.

class TipoDePagoAdmin(admin.ModelAdmin):
    fields = ['id_de_Pago', 'Efectivo', 'Tarjeta', 'Transferencia']
    list_display = ['id_de_Pago', 'Efectivo', 'Tarjeta', 'Transferencia']

class ProductoAdmin(admin.ModelAdmin):
    fields = ['id_Producto', 'Precio', 'Tamaño', 'Color']
    list_display = ['id_Producto', 'Precio', 'Tamaño', 'Color']

class TipoDeProductoAdmin(admin.ModelAdmin):
    fields = ['id_Tipo_de_producto', 'Nombre', 'Referencia', 'producto']
    list_display = ['id_Tipo_de_producto', 'Nombre', 'Referencia', 'producto']

class UsuarioAdmin(admin.ModelAdmin):
    fields = ['id_Usuario', 'Primer_nombre', 'Segundo_nombre', 'Primer_apellido', 'Segundo_apellido', 'Tipo_documento', 'Documento', 'Direccion', 'Telefono', 'Correo']
    list_display = ['id_Usuario', 'Primer_nombre', 'Segundo_nombre', 'Primer_apellido', 'Segundo_apellido', 'Tipo_documento', 'Documento', 'Direccion', 'Telefono', 'Correo']

class CompraAdmin(admin.ModelAdmin):
    fields = ['id_Compra', 'Cantidad', 'Valor', 'tipo_de_pago']
    list_display = ['id_Compra', 'Cantidad', 'Valor', 'tipo_de_pago']

class VentaAdmin(admin.ModelAdmin):
    fields = ['id_Venta', 'Valor', 'tipo_de_pago']
    list_display = ['id_Venta', 'Fecha', 'Valor', 'tipo_de_pago']

class MaterialAdmin(admin.ModelAdmin):
    fields = ['id_Material', 'Calidad', 'Tamaño', 'Color', 'Tipo', 'Nombre', 'Precio']
    list_display = ['id_Material', 'Calidad', 'Tamaño', 'Color', 'Tipo', 'Nombre', 'Precio']

admin.site.register(TipoDePago, TipoDePagoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoDeProducto, TipoDeProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Material, MaterialAdmin)