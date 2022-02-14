
from django.urls import path
from rest_framework.fields import URLField
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from vuelosApp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('refresh/', TokenRefreshView.as_view()),           # renovar el access token http://localhost:8000/refresh/     # Esta vista ya viene implementada en el paquete de django framework
    path('login/', TokenObtainPairView.as_view()),          # iniciar sesión http://localhost:8000/login/                # Esta vista ya viene implementada en el paquete de django framework

    path('user/', views.UserCreateView.as_view()),          # registra usuario http://localhost:8000/user/                              # Esta vista se implementa desde cero
    path('user/<int:pk>', views.UserDetailView.as_view()),  # obtener la info de un usuario http://localhost:8000/user/<int:pk>/        # Esta vista se implementa desde cero

    path('vuelos/create/', views.VueloListView.as_view()),          # registra un vuelo y lista todos http://localhost:8000/vuelo/                         # Esta vista se implementa desde cero
    path('vuelos/i/<int:pk>', views.VueloDetailView.as_view()),# consulta, actualiza o elimina un vuelo http://localhost:8000/vuelo/<int:pk>/         # Esta vista se implementa desde cero
    path('vuelos/d/<int:ciudad_d>', views.DestinoFilteredView.as_view(), name = "filtro_destino"), # consulta vuelos de acuerdo con el id de la ciudad de destino
    path('vuelos/o/<int:ciudad_o>', views.OrigenFilteredView.as_view(), name="filtro_origen"), # consulta vuelos de acuerdo con el id de la ciudad de destino

    path('reserva/create/', views.ReservaCreateView.as_view()),            # registra una reserva y lista todas http://localhost:8000/reserva/                      # utilizando generics
    path('reserva/<int:pk>', views.ReservaRetrieveView.as_view()),  # consulta, actualiza o elimina una reserva http://localhost:8000/reserva/<int:pk>/      # utilizando generics
    path('reserva/list/<int:user>', views.ReservaFilteredView.as_view()),  # consulta, actualiza o elimina una reserva http://localhost:8000/reserva/<int:pk>/      # utilizando generics
    path('reserva/update/<int:user>/<int:pk>', views.ReservaUpdateView.as_view()),
    path('reserva/remove/<int:user>/<int:pk>', views.ReservaDeleteView.as_view()),

    path('ciudad/', views.CiudadList.as_view()),            # registra una ciudad y lista todas http://localhost:8000/ciudad/                      # utilizando generics
    path('ciudad/<int:pk>', views.CiudadDetail.as_view()),  # consulta, actualiza o elimina una ciudad http://localhost:8000/ciudad/<int:pk>/      # utilizando generics
    
    
]