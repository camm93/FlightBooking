from vuelosApp.models.tarjeta import Tarjeta, TIPOS_OPT
from rest_framework import serializers


class TarjetaSerializer(serializers.ModelSerializer):

    tipo = serializers.ChoiceField(choices=TIPOS_OPT)

    class Meta:
        model = Tarjeta
        fields = ["id_tarjeta","nombre_propietario", "fecha_vencimiento", "codigo", "tipo"]
