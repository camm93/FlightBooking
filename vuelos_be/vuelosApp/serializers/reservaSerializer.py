from vuelosApp.models.reserva import Reserva
from rest_framework import serializers


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Reserva
        fields = ["id_reserva", "fecha", "last_updated", "vuelo", "cliente", "puestos"]

    def create(self, validated_data):
        reservaInstance = Reserva.objects.create(**validated_data)
        return reservaInstance
