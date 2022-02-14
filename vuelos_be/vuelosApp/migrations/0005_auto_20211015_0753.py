# Generated by Django 3.2.7 on 2021-10-15 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vuelosApp', '0004_alter_ciudades_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudades',
            name='nombre',
            field=models.CharField(choices=[('1', 'Amazonía'), ('2', 'Barranquilla'), ('3', 'Bogotá'), ('4', 'Bucaramanga'), ('5', 'Cali'), ('6', 'Cartagena'), ('7', 'Cúcuta'), ('8', 'Ibagué'), ('9', 'Medellín'), ('10', 'Neiva'), ('11', 'Pamplona'), ('12', 'Quibdó'), ('13', 'Risaralda'), ('14', 'San Andrés'), ('15', 'Villavicencio')], default=('3', 'Bogotá'), max_length=30, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='vuelo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserva_vuelo', to='vuelosApp.vuelos'),
        ),
    ]
