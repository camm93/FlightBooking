from django.db import models
from .user import User
from random import randint


TIPOS_OPT = (
    ('A', "American Express"),
    ('B', "Bank of America"),
    ('D', "Diners Club"),
    ('M', "MasterCard"),
    ('V', "Visa"),
)


def code_gen():
    return str(randint(100,999))


class Tarjeta(models.Model):

    id_tarjeta = models.BigAutoField(primary_key=True) 
    nombre_propietario = models.CharField('Nombre_Propietario', max_length=30, blank=True)
    fecha_vencimiento = models.DateField("Fecha_Vencimiento", null=True,       
                                         blank=True)
    codigo = models.CharField(default=code_gen, blank=True, max_length=3)
    tipo = models.CharField("Tipo", max_length=1, choices=TIPOS_OPT,            
                            help_text="""
                            Pick one out of five possible card types. 'A' American Express, 
                            'B' Bank of America, 'D' Diners Club, 'M' MasterCard and 'V' Visa.
                            """, blank=True, default=TIPOS_OPT[0][0])
    cliente = models.ForeignKey(User, related_name="tarjetas", 
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<Tarjeta ID: {self.id_tarjeta}, Cliente: {self.cliente}, Tipo: {self.get_tipo_display()}'
