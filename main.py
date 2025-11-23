from clases.subclaseAve import Ave
from clases.subclaseElefante import Elefante
from clases.subclaseLeon import Leon

from modulo_reservas_y_visitas.subclaseReservaDiurna import ReserveDiurna
from modulo_reservas_y_visitas.subClaseReservaNocturna import ReservaNocturna




def reproducir_sonidos(lista_animales):
    for animal in lista_animales:
        print(animal.sonido())

def animalesInfo(lista_animales):
    for animal in lista_animales:
        print(animal.informacion())

pajaro = Ave("Rodrigo", "pajaro", 2, "la casa de simon", "de las que vuelan")
leon = Leon("Rodolfo", "peludo", 3, "el congo", 45)
elefante = Elefante("anastasio", "gris", 34, "Groenlandia", 50)


reproducir_sonidos([pajaro, leon, elefante])
animalesInfo([pajaro, leon, elefante])

reserva1 = ReserveDiurna("Carlos Perez", (10,6,2025), 4, 2)
reserva2 = ReservaNocturna("Marina Lopez", (2023,6,12), 2, 1)

#poliformismo reservas
reservas = [reserva1, reserva2]

for reserva in reservas:
    print(reserva.costoTotal())