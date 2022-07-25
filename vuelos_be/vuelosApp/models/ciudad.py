from django.db import models


CIUDADES_OPT = (
    ("1", "Amazonía"),
    ("2", "Barranquilla"),
    ("3", 'Bogotá'),
    ("4", "Bucaramanga"),
    ("5", "Cali"),
    ("6", "Cartagena"),
    ("7", "Cúcuta"),
    ("8", "Ibagué"),
    ("9", "Medellín"),
    ("10", "Neiva"),
    ("11", "Pamplona"),
    ("12", "Quibdó"),
    ("13", "Risaralda"),
    ("14", "San Andrés"),
    ("15", "Villavicencio")
)


class Ciudad(models.Model):

    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, choices=CIUDADES_OPT, unique=True)

    def __str__(self):
        return f"{self.get_nombre_display()}"
