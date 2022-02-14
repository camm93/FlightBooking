from django.db import models
from django.db.models.deletion import CASCADE
from .user import User
from .vuelos import Vuelos

class Reservas(models.Model):
    id_reservas  = models.AutoField(primary_key = True)
    fecha        = models.DateField(auto_now_add = True, blank=True)                    
    last_updated = models.DateTimeField(auto_now = True, blank=True)                    
    vuelo        = models.ForeignKey(Vuelos, related_name = "reserva_vuelo", on_delete = CASCADE)
    cliente      = models.ForeignKey(User, related_name = "reserva_user", on_delete = CASCADE)