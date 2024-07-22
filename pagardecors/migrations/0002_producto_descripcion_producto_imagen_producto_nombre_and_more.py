# Generated by Django 4.1.3 on 2024-07-18 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagardecors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='Cantidad',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='Fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='Valor',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='tipo_de_pago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagardecors.tipodepago'),
        ),
        migrations.AlterField(
            model_name='material',
            name='Calidad',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Color',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Nombre',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Precio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Tamaño',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Tipo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Color',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='Precio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Tamaño',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tipodepago',
            name='Efectivo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tipodepago',
            name='Tarjeta',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tipodepago',
            name='Transferencia',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Correo',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Documento',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Primer_apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Primer_nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Segundo_apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Segundo_nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Telefono',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Tipo_documento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_Usuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='venta',
            name='Fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='Valor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='tipo_de_pago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagardecors.tipodepago'),
        ),
    ]