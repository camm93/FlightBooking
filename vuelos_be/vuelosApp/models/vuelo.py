from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from .ciudad import Ciudad
from django.utils.translation import gettext_lazy as _


ESTADOS_OPT = (
    ('A', "Activo"),
    ('C', "Cancelado"),
    ('F', "Finalizado"),
    ('R', "Retrasado"),
)


def two_hours_hence():
    return timezone.now() + timezone.timedelta(hours=2)


class Vuelo(models.Model):
    id_vuelo = models.AutoField(primary_key=True)
    fecha_salida = models.DateTimeField(default=timezone.now, blank=True)
    fecha_llegada = models.DateTimeField(default=two_hours_hence, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2,
                                 default=500000, blank=True)
    estado = models.CharField("Estado_Vuelo", choices=ESTADOS_OPT,
                              max_length=1, help_text=_("""
                              Seleccione una de los 4 estados posibles del vuelo. 
                              'A' para Activo, 'C' Cancelado, 'F' Finalizado y 'R' Retrasado."""),
                              default=ESTADOS_OPT[0][0])         
    _cupos = models.PositiveIntegerField(default=50, blank=True)
    company = models.CharField(max_length=30)                      
    destino = models.ForeignKey(Ciudad, related_name="vuelos_destino",    
                                on_delete=CASCADE)
    origen = models.ForeignKey(Ciudad, related_name="vuelos_origen",      
                               on_delete=CASCADE)

    @property
    def cupos(self):
        return self._cupos

    @cupos.setter
    def cupos(self, cupos):
        self._cupos = cupos

    def __str__(self):
        return "Vuelo ID: %i, Compañía: %s, Origen: %s, Destino: %s" % (self.id_vuelo, 
                self.company, self.origen, self.destino)
