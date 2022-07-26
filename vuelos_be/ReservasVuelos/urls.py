from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from vuelosApp import views


schema_view = get_schema_view(
   openapi.Info(
      title="Flight Booking API",
      default_version='v1',
      description="A REST API for Flight Ticket Reservation using Django - DRF.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="camm93@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('refresh/', TokenRefreshView.as_view()),  # Renovar el access token. Built-in view
    path('login/', TokenObtainPairView.as_view()),  # Iniciar sesión. Built-in view.

    path('user/', views.UserCreateView.as_view()),  # Registro de usuario (User Sign-Up)
    path('user/<int:pk>', views.UserDetailView.as_view()),  # Detalles del usuario

    path('vuelos/create/', views.VueloCreateView.as_view()),  # Crea un vuelo nuevo (AdminUser)
    path('vuelos/list/', views.VueloListView.as_view()),  # Lista todos los vuelos existentes.
    path('vuelos/manage/<int:pk>', views.VueloExtraView.as_view()),  # Funcionalidades extra (AdminUser)
    path('vuelos/i/<int:pk>', views.VueloDetailView.as_view()),  # Consulta un vuelo por ID
    path('vuelos/d/<int:ciudad_d>', views.DestinoFilteredView.as_view(), name="vuelos_by_destino"),  # Vuelos filtrados por destino
    path('vuelos/o/<int:ciudad_o>', views.OrigenFilteredView.as_view(), name="vuelos_by_origen"),  # Vuelos filtrados por origen

    path('reserva/create/', views.ReservaCreateView.as_view()),  # Registra una reserva del usuario
    path('reserva/list/<int:user>', views.ReservaListView.as_view()),  # Consulta todas las reservas del usuario.
    path('reserva/update/<int:user>/<int:pk>', views.ReservaUpdateView.as_view()),  # Actualiza la cantidad de puestos en una reserva.
    path('reserva/remove/<int:user>/<int:pk>', views.ReservaDeleteView.as_view()),  # Elimina una reserva.

    path('ciudad/create/', views.CiudadCreate.as_view()),  # Crea una nueva ciudad(AdminUser)
    path('ciudad/list/', views.CiudadList.as_view()),  # Lista todas las ciudades existentes
    path('ciudad/<int:pk>', views.CiudadDetail.as_view()),  # Consulta una ciudad, la actualiza o la elimina (AdminUser)

    path('swagger<format>.json|.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
