from rest_framework import serializers
from vuelosApp.models.vuelos import Vuelos

class VuelosSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Vuelos
        fields = ["id_vuelo","fecha_salida", "fecha_llegada", "precio", "estado",  "cupos", "company", "destino", "origen"]