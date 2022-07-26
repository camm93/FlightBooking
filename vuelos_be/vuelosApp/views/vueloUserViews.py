"""
These views intentionally lack authentication because all users should be able to search for flights.
"""
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from vuelosApp.models.vuelo import Vuelo
from vuelosApp.serializers.vueloSerializer import VueloSerializer


class DestinoFilteredView(generics.ListAPIView):
    """Filters flights by destination.
    """
    serializer_class = VueloSerializer

    @swagger_auto_schema(operation_summary="Lists Flights by Destiny.")
    def get_queryset(self):
        ciudad_destino = self.request.GET.get("ciudad_d") 
        if (ciudad_destino != None or ciudad_destino != ""):
            return Vuelo.objects.filter(destino_id=self.kwargs["ciudad_d"])


class OrigenFilteredView(generics.ListAPIView):
    """Filters flights by origin.
    """
    serializer_class = VueloSerializer

    @swagger_auto_schema(operation_summary="Lists Flights by Origin.")
    def get_queryset(self):
        ciudad_origen = self.request.GET.get("ciudad_o")
        if (ciudad_origen != None or ciudad_origen != ""):
            return Vuelo.objects.filter(origen_id=self.kwargs["ciudad_o"])


class VueloDetailView(generics.ListAPIView):
    """Retrieves a flight by Id.
    ListAPIView was intentionally chosen over RetrieveAPIView for improved
    functionality in web component.
    """
    serializer_class = VueloSerializer

    @swagger_auto_schema(operation_summary="Retrieve Flight by ID.")
    def get_queryset(self):
        queryset = Vuelo.objects.filter(id_vuelo=self.kwargs["pk"])
        return queryset
