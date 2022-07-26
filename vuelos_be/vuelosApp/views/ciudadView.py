from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from vuelosApp.models.ciudad import Ciudad
from vuelosApp.serializers.ciudadSerializer import CiudadSerializer


class CiudadCreate(generics.CreateAPIView):
    """Allows to create new cities.
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = [IsAdminUser]


class CiudadList(generics.ListAPIView):
    """Lists all existing cities.
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer


class CiudadDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update or Delete a city. For admin users only.
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = [IsAdminUser]
