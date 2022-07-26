from django.contrib import admin
from django.urls import include, path
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

city_patterns = [
    path('create/', views.CiudadCreate.as_view()),  # Crea una nueva ciudad(AdminUser)
    path('list/', views.CiudadList.as_view()),  # Lista todas las ciudades existentes
    path('<int:pk>', views.CiudadDetail.as_view()),  # Consulta una ciudad, la actualiza o la elimina (AdminUser)
]

flight_patterns = [
    path('create/', views.VueloCreateView.as_view()),  # Crea un vuelo nuevo (AdminUser)
    path('list/', views.VueloListView.as_view()),  # Lista todos los vuelos existentes.
    path('manage/<int:pk>', views.VueloExtraView.as_view()),  # Funcionalidades extra (AdminUser)
    path('i/<int:pk>', views.VueloDetailView.as_view()),  # Consulta un vuelo por ID
    path('d/<int:ciudad_d>', views.DestinoFilteredView.as_view(), name="vuelos_by_destino"),  # Vuelos filtrados por destino
    path('o/<int:ciudad_o>', views.OrigenFilteredView.as_view(), name="vuelos_by_origen"),  # Vuelos filtrados por origen
]

reservation_patterns = [
    path('create/', views.ReservaCreateView.as_view()),  # Registra una reserva del usuario
    path('list/<int:user>', views.ReservaListView.as_view()),  # Consulta todas las reservas del usuario.
    path('update/<int:user>/<int:pk>', views.ReservaUpdateView.as_view()),  # Actualiza la cantidad de puestos en una reserva.
    path('remove/<int:user>/<int:pk>', views.ReservaDeleteView.as_view()),  # Elimina una reserva.
]

user_patterns = [
    path('', views.UserCreateView.as_view()),  # Registro de usuario (User Sign-Up)
    path('<int:pk>', views.UserDetailView.as_view()),  # Detalles del usuario
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ciudad/', include(city_patterns)),
    path('login/', TokenObtainPairView.as_view()),  # Iniciar sesión. Built-in view.
    path('reserva/', include(reservation_patterns)),
    path('user/', include(user_patterns)),
    path('vuelos/', include(flight_patterns)),
    path('refresh/', TokenRefreshView.as_view()),  # Renovar el access token. Built-in view
    path('swagger<format>.json|.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
