from vuelosApp.models.ciudad import Ciudad
from vuelosApp.serializers.ciudadSerializer import CiudadSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class CiudadList(generics.ListCreateAPIView):
    """Allows to create new cities and list all existing ones.
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = [IsAdminUser]


class CiudadDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update or Delete a city."""
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = [IsAdminUser]
    