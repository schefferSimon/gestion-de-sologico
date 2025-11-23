from clase_reserva import Reserva

class ReservaEducativa(Reserva):
    def __init__(self, nombreVisitante, fecha, cantidad_de_personas, duracion_horas):
        super().__init__(nombreVisitante, fecha, cantidad_de_personas, duracion_horas)

    def costo_total(self):
        #precio por persona
        costo = self.costo_total * self.__cantidad_de_personas * 0.60
        return costo
    
    def descripcion_reserva(self):
        return f"Reserva Educativa\n{super().descripcion_reserva()}"