from django.contrib import admin
from .models.ciudades import Ciudades
from .models.reservas import Reservas
from .models.tarjetas import Tarjetas
from .models.user import User
from .models.vuelos import Vuelos

admin.site.register(Ciudades)
admin.site.register(Reservas)
admin.site.register(Tarjetas)
admin.site.register(User)
admin.site.register(Vuelos)
