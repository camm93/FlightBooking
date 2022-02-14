from django.conf                        import settings
from rest_framework                     import generics, status
from rest_framework.response            import Response
from rest_framework_simplejwt.backends  import TokenBackend
from rest_framework.permissions         import IsAuthenticated

from vuelosApp.models.reservas import Reservas
from vuelosApp.models.user     import User
from vuelosApp.serializers.reservasSerializer import ReservaSerializer


class ReservaCreateView(generics.CreateAPIView):
    serializer_class = ReservaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        #print(valid_data['user_id'])
        #print(valid_data)
        #print(request.data)
        
        if "cliente" not in request.data:
            stringResponse = {"Error": "'cliente' is not in request.data"}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        if valid_data["user_id"] != int(request.data['cliente']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = ReservaSerializer(data = request.data)

        serializer.is_valid(raise_exception = True)
        serializer.save()
        print(serializer.data)

        return Response("Reserva exitosa", status=status.HTTP_201_CREATED)


class ReservaFilteredView(generics.ListAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data["user_id"] != int(self.kwargs['user']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Reservas.objects.filter(cliente = self.kwargs["user"])
        return queryset


class ReservaDeleteView(generics.DestroyAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = (IsAuthenticated,)
    def delete(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data["user_id"] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)


class ReservaUpdateView(generics.UpdateAPIView):
    """Sólamente implementadas y utilizadas desde el back"""
    queryset = Reservas.objects.all()
    serializer_class = ReservaSerializer
    """   
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data["user_id"] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)        
    """


class ReservaRetrieveView(generics.RetrieveAPIView):
    """ Esta vista consulta una reserva basado en su pk
        No implementada en el front.
        Sólo para revisión en el back
    """
    queryset = Reservas.objects.all()
    serializer_class = ReservaSerializer
    """permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data["user_id"] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)
    """

