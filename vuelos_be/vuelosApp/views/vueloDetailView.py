from django.http.response import Http404
from rest_framework import status, views
from rest_framework.response import Response
from vuelosApp.models.vuelos import Vuelos
from vuelosApp.serializers.vuelosSerializer import VuelosSerializer

class VueloDetailView(views.APIView):
    
    """Consultar, actualizar o eliminar un vuelo"""

    def get_object(self, pk):
        try:
            return Vuelos.objects.get(pk = pk)
        except Vuelos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        vuelo = self.get_object(pk)
        serializer = VuelosSerializer(vuelo)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        vuelo = self.get_object(pk)
        serializer = VuelosSerializer(vuelo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        vuelo = self.get_object(pk)
        vuelo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)