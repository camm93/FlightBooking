from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from vuelosApp.models.reserva import Reserva
from vuelosApp.serializers.reservaSerializer import ReservaSerializer
from vuelosApp.app_business_logic import FlightBooking

from drf_yasg.utils import swagger_auto_schema


class ReservaCreateView(generics.CreateAPIView):
    """Makes a flight reservation after user authentication.
    """
    serializer_class = ReservaSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(operation_summary="Make a reservation.")
    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if "cliente" not in request.data:
            stringResponse = {"Error": "'cliente' is not in request.data"}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if valid_data["user_id"] != int(request.data['cliente']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            puestos = serializer.data.get("puestos")
            vuelo_id = serializer.data.get("vuelo")
            FlightBooking.reserve_seats(vuelo_id=vuelo_id, puestos=puestos)
            return Response("Reservation Successful", status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservaListView(generics.ListAPIView):
    """Lists all reservations of a given user. Authentication required.
    """
    serializer_class = ReservaSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data["user_id"] != int(self.kwargs['user']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Reserva.objects.filter(cliente=self.kwargs["user"])
        return queryset


class ReservaDeleteView(generics.DestroyAPIView):
    """Deletes a flight reservation after user authentication.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(operation_summary="Delete a reservation.")
    def delete(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data["user_id"] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        FlightBooking.remove_reservation(reserva_id=self.kwargs["pk"])
        return super().destroy(request, *args, **kwargs)


class ReservaUpdateView(generics.UpdateAPIView):
    """Updates the number of seats on a given reservation. Requires authentication.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(operation_summary="Patch a reservation (Number of seats).")
    def patch(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data["user_id"] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        FlightBooking.update_seats(reserva_id=self.kwargs["pk"], new_puestos=request.data["puestos"]) 
        return super().partial_update(request, *args, **kwargs)        


