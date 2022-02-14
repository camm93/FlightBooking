from django.conf                        import settings
from rest_framework                     import generics, request, status
from rest_framework.response            import Response
from rest_framework                     import filters
from django.db.models                   import Q

from vuelosApp.models.vuelos                import Vuelos
from vuelosApp.serializers.vuelosSerializer import VuelosSerializer

class DestinoFilteredView(generics.ListAPIView):
    """ Las vistas de Vuelos no tienen autenticación, puesto que cualquier
    usuario, incluso no registrados, pueden consultar vuelos"""
    serializer_class = VuelosSerializer
    def get_queryset(self):

        ciudad_destino= self.request.GET.get("ciudad_d")
        print(ciudad_destino)
        
        if (ciudad_destino != None or ciudad_destino != ""):
            return Vuelos.objects.filter(destino_id = self.kwargs["ciudad_d"])

class OrigenFilteredView(generics.ListAPIView):
    serializer_class = VuelosSerializer
    def get_queryset(self):
        ciudad_origen = self.request.GET.get("ciudad_o")
        print(ciudad_origen)
        if (ciudad_origen != None or ciudad_origen != ""):
            return Vuelos.objects.filter(origen_id = self.kwargs["ciudad_o"])
      
        
class VueloDetailView(generics.ListAPIView):
    queryset = Vuelos.objects.all()
    serializer_class = VuelosSerializer
    def get_queryset(self):
        queryset = Vuelos.objects.filter(id_vuelo = self.kwargs["pk"])
        return queryset


class VueloCreateView(generics.CreateAPIView):
    queryset = Vuelos.objects.all()
    serializer_class = VuelosSerializer


class VueloUpdateView(generics.UpdateAPIView):
    queryset = Vuelos.objects.all()
    serializer_class = VuelosSerializer


class VueloDeleteView(generics.DestroyAPIView):
    queryset = Vuelos.objects.all()
    serializer_class = VuelosSerializer