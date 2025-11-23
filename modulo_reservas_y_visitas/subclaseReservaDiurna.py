from modulo_reservas_y_visitas.clase_reserva import Reserva

class ReserveDiurna(Reserva):
    def __init__(self, nombreVisitante, fecha, cantidad_de_personas, duracion_horas):
        super().__init__(nombreVisitante, fecha, cantidad_de_personas, duracion_horas)

    
    def costo_total(self):
        return self.__costo_base * 1.20
    
