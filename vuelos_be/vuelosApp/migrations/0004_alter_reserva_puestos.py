# Generated by Django 3.2.7 on 2022-03-15 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuelosApp', '0003_auto_20220313_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='puestos',
            field=models.IntegerField(default=1),
        ),
    ]