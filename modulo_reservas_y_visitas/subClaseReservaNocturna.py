from modulo_reservas_y_visitas.clase_reserva import Reserva

class ReservaNocturna(Reserva):
    def __init__(self, nombreVisitante, fecha, cantidad_de_personas, duracion_horas):
        super().__init__(nombreVisitante, fecha, cantidad_de_personas, duracion_horas)

    def costo_total(self):
        costo =  self.__costo_base * 1.35
        
        #tarifa minima
        if costo < 5000:
            costo = 5000
        return costo
    
    def descripcion_reserva(self):
        return f"Reserva Nocturna\n{super().descripcion_reserva()} costo: { self.costo_total()}"