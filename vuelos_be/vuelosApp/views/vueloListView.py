from rest_framework import status, views
from rest_framework.response import Response
from vuelosApp.serializers.vuelosSerializer import VuelosSerializer
from vuelosApp.models.vuelos import Vuelos

class VueloListView(views.APIView):

    """ Lista todo los vuelos o crea uno nuevo """

    def get(self, request, format = None):
        queryset         = Vuelos.objects.all()
        serializer_class = VuelosSerializer(queryset, many = True)
        return Response(serializer_class.data)


    def post(self, request, format = None):
        serializer = VuelosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)