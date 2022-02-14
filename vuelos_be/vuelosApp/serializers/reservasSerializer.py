from vuelosApp.models.reservas import Reservas
from rest_framework import serializers

class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Reservas
        fields = ["id_reservas","fecha", "last_updated", "vuelo", "cliente"]
