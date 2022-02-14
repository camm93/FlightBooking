from django.db import models
from .user import User

TIPOS_OPT = (
    ('A', "American Express"),
    ('B', "Bank of America"),
    ('D', "Diners Club"),
    ('M', "MasterCard"),
    ('V', "Visa"),
)

class Tarjetas(models.Model):
    id_tarjetas        = models.BigAutoField(primary_key = True) 
    nombre_propietario = models.CharField('Nombre', max_length = 30, blank = True)
    fecha_vencimiento  = models.DateField("Fecha_Vencimiento", null = True, blank = True)
    codigo             = models.IntegerField(default = 0, blank = True)
    tipo               = models.CharField("Tipo", max_length = 1, choices = TIPOS_OPT, help_text = """
                                     Seleccione una de las 5 posibles tarjetas. 'A' American Express, 
                                     'B' Bank of America, 'D' Diners Club, 'M' MasterCard y 'V' Visa """, blank = True, default=TIPOS_OPT[0])             # Modificado)
    cliente            = models.ForeignKey(User, related_name = "tarjetas", on_delete = models.CASCADE)
