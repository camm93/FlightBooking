# Generated by Django 3.2.7 on 2021-10-30 02:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vuelosApp', '0015_auto_20211028_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelos',
            name='cupos',
            field=models.PositiveIntegerField(blank=True, default=50),
        ),
        migrations.AlterField(
            model_name='vuelos',
            name='fecha_llegada',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vuelos',
            name='fecha_salida',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vuelos',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, default=500000, max_digits=10),
        ),
    ]
