from rest_framework import serializers
from vuelosApp.models.vuelo import Vuelo

class VueloSerializer(serializers.ModelSerializer):

    class Meta:

        model = Vuelo
        fields = ["id_vuelo", "fecha_salida", "fecha_llegada", "precio", "estado",  "cupos", "company", "destino", "origen"]