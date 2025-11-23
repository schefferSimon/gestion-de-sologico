class Reserva:
    def __init__(self, nombreVisitante, fecha , cantidad_de_personas, duracion_horas):
        if not isinstance(nombreVisitante, str) and nombreVisitante == "":
            raise ValueError("nombre vacio")
        if not len(fecha) == 3 and isinstance(fecha, tuple):
            raise ValueError("fecha vacia")
        else:
            for i in fecha:
                if not isinstance(i, int):
                    raise TypeError("El contenido de la fecha debe ser entero.")
                
                dd = fecha(0) 
                mm = fecha(1)
                aa = fecha(2)
                self.__fecha = aa + "-" + mm + "-" + dd
                print(self.__fecha) #Para debugear
        if not isinstance(cantidad_de_personas, int) and cantidad_de_personas > 0 :
            raise ValueError("las cantidad de personas tiene que ser mayor a cero")

        self.__visitante = nombreVisitante
        #self.__fecha = fecha
        self.__duracion_horas = duracion_horas
        self.__cantidad_de_personas = cantidad_de_personas
        self.__costo_base = 10000
    
    def getCosto_base(self):
        return self.__costo_base
        

    def descripcion_reserva(self):
        return f"Reserva normal\nel visitante: {self.__visitante}, fecha de reserva: {self.__fecha}, horas {self.__duracion_horas}, cantidad de personas: {self.__cantidad_de_personas}"
    
    def costo_total(self):
        return self.__costo_base * self.__cantidad_de_personas * self.__duracion_horas
    
    #----------------terminar-------------------
    @staticmethod
    def validar_fecha(fecha):
        reloj = 0
        for i in fecha:
            reloj += 1
            if reloj == 5:
                if i == "-":
                    continue
                else : 
                    return False
            elif reloj == 8 :
                if i == "-":
                    continue
                else:
                    return False
                    
        return True
    
    def mostrarCostos(reservas):
        for reserva in reservas:
            print(reserva.costoTotal())

    


    
