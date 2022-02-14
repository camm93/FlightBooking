from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from .ciudades import Ciudades

ESTADOS_OPT = (
    ('A', "Activo"),
    ('C', "Cancelado"),
    ('F', "Finalizado"),
    ('R', "Retrasado"),
)

class Vuelos(models.Model):
    id_vuelo      = models.AutoField(primary_key = True)
    fecha_salida  = models.DateTimeField(default = timezone.now, blank=True)
    fecha_llegada = models.DateTimeField(default = timezone.now, blank = True)
    precio        = models.DecimalField(max_digits = 10, decimal_places = 2, default=500000, blank=True)
    estado        = models.CharField("Estado_Vuelo", choices = ESTADOS_OPT, max_length = 1, help_text="""
                                     Seleccione una de los 4 estados posibles del vuelo. 'A' para Activo, 
                                     'C' Cancelado, 'F' Finalizado y 'R' Retrasado """)         
    cupos         = models.PositiveIntegerField(default = 50, blank = True)
    company       = models.CharField(max_length = 30)                      
    destino       = models.ForeignKey(Ciudades, related_name = "vuelos_destino", on_delete = CASCADE)
    origen        = models.ForeignKey(Ciudades, related_name = "vuelos_origen", on_delete = CASCADE)     
