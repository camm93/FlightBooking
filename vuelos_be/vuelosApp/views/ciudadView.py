from vuelosApp.models.ciudades import Ciudades
from vuelosApp.serializers.ciudadesSerializer import CiudadesSerializer
from rest_framework import generics

class CiudadList(generics.ListCreateAPIView):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer

class CiudadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer
    