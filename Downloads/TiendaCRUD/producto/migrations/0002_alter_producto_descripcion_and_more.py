# Generated by Django 4.2.7 on 2023-11-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=200, verbose_name='Descripcion del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='existencias',
            field=models.IntegerField(verbose_name='Existencias  del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.TextField(max_length=50, verbose_name='Nombre del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Precio del producto'),
        ),
    ]