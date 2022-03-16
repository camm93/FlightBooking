from django.db import models
from django.db.models.deletion import CASCADE
from .user import User
from .vuelo import Vuelo


class Reserva(models.Model):

    id_reserva = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True, blank=True)                    
    last_updated = models.DateTimeField(auto_now=True,      
                                        blank=True)                    
    puestos = models.IntegerField(default=1, blank=False)                                
    vuelo = models.ForeignKey(Vuelo, related_name="reserva_vuelo",             
                              on_delete=CASCADE)
    cliente = models.ForeignKey(User, related_name="reserva_user",      
                                on_delete=CASCADE)
    
    def __str__(self):
        return f'Reserva N° {self.id_reserva}. Cliente: {self.cliente},\
             Vuelo_ID: {self.vuelo}, Cantidad: {self.puestos}'