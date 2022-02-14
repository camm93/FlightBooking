from rest_framework import serializers
from rest_framework.fields import ChoiceField
from vuelosApp.models.ciudades import CIUDADES_OPT, Ciudades


class CiudadesSerializer(serializers.ModelSerializer):
    nombre = serializers.ChoiceField(choices = CIUDADES_OPT, source = 'get_nombre_display', read_only = True)
    #nombre = serializers.CharField(source = 'get_nombre_display')

    class Meta:
        model  = Ciudades
        fields = ["id_ciudad", "nombre"]
    
