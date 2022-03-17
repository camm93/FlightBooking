from django.http.response import Http404
from rest_framework import status, views, generics
from rest_framework.response import Response
from vuelosApp.models.vuelo import Vuelo
from vuelosApp.serializers.vueloSerializer import VueloSerializer
from rest_framework.permissions import IsAdminUser

from drf_yasg.utils import swagger_auto_schema


class VueloExtraView(views.APIView):
    """Consultar, actualizar o eliminar un vuelo.
    """
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Vuelo.objects.get(pk=pk)
        except Vuelo.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_summary="Retrieve a Flight.")
    def get(self, request, pk, format=None):
        vuelo = self.get_object(pk)
        serializer = VueloSerializer(vuelo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update a Flight.")
    def put(self, request, pk, format=None):
        vuelo = self.get_object(pk)
        serializer = VueloSerializer(vuelo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Delete a Flight.")
    def delete(self, request, pk, format=None):
        vuelo = self.get_object(pk)
        vuelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VueloListView(generics.ListCreateAPIView):
    """Lists all existing flights.
    Creates a new flight. AdminUsers Only.
    """    
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer
    permission_classes = [IsAdminUser]