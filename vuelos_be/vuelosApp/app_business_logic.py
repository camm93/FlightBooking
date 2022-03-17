from vuelosApp.models.reserva import Reserva
from vuelosApp.models.vuelo import Vuelo


class FlightBooking():

    @staticmethod
    def reserve_seats(vuelo_id, puestos):
        vuelo = Vuelo.objects.get(id_vuelo=vuelo_id)
        vuelo.cupos -= puestos
        vuelo.save()

    @staticmethod
    def remove_reservation(reserva_id):
        reserva = Reserva.objects.get(id_reserva=reserva_id)
        vuelo = Vuelo.objects.get(id_vuelo=reserva.vuelo.id_vuelo)
        vuelo.cupos += reserva.puestos 
        vuelo.save()

    @staticmethod
    def update_seats(reserva_id, new_puestos):
        reserva = Reserva.objects.get(id_reserva=reserva_id)
        old_puestos = reserva.puestos
        vuelo = Vuelo.objects.get(id_vuelo=reserva.vuelo.id_vuelo)
        vuelo.cupos += (old_puestos - new_puestos)
        vuelo.save()
    

