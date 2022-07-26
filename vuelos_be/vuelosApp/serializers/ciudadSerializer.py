from rest_framework import serializers
from vuelosApp.models.ciudad import CIUDADES_OPT, Ciudad


class CiudadSerializer(serializers.ModelSerializer):

    nombre = serializers.ChoiceField(choices=CIUDADES_OPT, source='get_nombre_display', read_only=True)

    class Meta:
        model  = Ciudad
        fields = ["id_ciudad", "nombre"]
