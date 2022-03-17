"""
Estas vistas de Vuelos no tienen autenticación, puesto que cualquier
usuario, incluso no registrados, pueden consultar vuelos.
"""


from rest_framework import generics
from vuelosApp.models.vuelo import Vuelo
from vuelosApp.serializers.vueloSerializer import VueloSerializer
from drf_yasg.utils import swagger_auto_schema

class DestinoFilteredView(generics.ListAPIView):
    """Filters flights by destination.
    """
    serializer_class = VueloSerializer

    @swagger_auto_schema(operation_summary="Lists Flights by Destiny.")
    def get_queryset(self):
        ciudad_destino = self.request.GET.get("ciudad_d")
        print(ciudad_destino)     
        if (ciudad_destino != None or ciudad_destino != ""):
            return Vuelo.objects.filter(destino_id=self.kwargs["ciudad_d"])


class OrigenFilteredView(generics.ListAPIView):
    """Filters flights by origin.
    """
    serializer_class = VueloSerializer

    @swagger_auto_schema(operation_summary="Lists Flights by Origin.")
    def get_queryset(self):
        ciudad_origen = self.request.GET.get("ciudad_o")
        print(ciudad_origen)
        if (ciudad_origen != None or ciudad_origen != ""):
            return Vuelo.objects.filter(origen_id=self.kwargs["ciudad_o"])
      
        
class VueloDetailView(generics.ListAPIView):
    """Retrieves a flight by Id.
    ListAPIView was intentionally chosen over RetrieveAPIView for improved
    functionality in web component.
    """
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer

    @swagger_auto_schema(operation_summary="Retrieve Flight by ID.")
    def get_queryset(self):
        queryset = Vuelo.objects.filter(id_vuelo=self.kwargs["pk"])
        return queryset
