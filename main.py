from clases.subclaseAve import Ave
from clases.subclaseElefante import Elefante
from clases.subclaseLeon import Leon

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