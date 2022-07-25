from django.contrib import admin
from .models.ciudad import Ciudad
from .models.reserva import Reserva
from .models.tarjeta import Tarjeta
from .models.user import User
from .models.vuelo import Vuelo


class UserAdmin(admin.ModelAdmin):
    list_display = ["id_user", "username", "email", "is_staff", "date_joined"]
    list_filter = ["date_joined", "is_staff"]


class VueloAdmin(admin.ModelAdmin):
    list_display = [
        "id_vuelo", "fecha_salida", "fecha_llegada", "estado", "company",
        "destino", "origen"
    ]
    list_filter = ["estado", "company"]


class TarjetaAdmin(admin.ModelAdmin):
    list_display = [
        "id_tarjeta", "tipo", "cliente"
    ]


class CiudadAdmin(admin.ModelAdmin):
    list_display = [
        "id_ciudad", "nombre"
    ]


class ReservaAdmin(admin.ModelAdmin):
    list_display = [
        "id_reserva", "last_updated", "vuelo", "cliente", "puestos"
    ]


admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Tarjeta, TarjetaAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Vuelo, VueloAdmin)
