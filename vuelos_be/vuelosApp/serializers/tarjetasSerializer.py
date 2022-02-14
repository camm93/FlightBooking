from rest_framework.fields import ChoiceField
from vuelosApp.models.tarjetas import Tarjetas, TIPOS_OPT
from rest_framework import serializers

class TarjetasSerializer(serializers.ModelSerializer):
    tipo = serializers.ChoiceField(choices= TIPOS_OPT)
    class Meta:
        model  = Tarjetas
        fields = ["id_tarjetas","nombre_propietario", "fecha_vencimiento", "codigo", "tipo"]