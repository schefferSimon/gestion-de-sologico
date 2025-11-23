from clases.claseAnimal import Animal

class Elefante(Animal):
    def __init__(self, nombre, especie, edad, habitat, tamano):
        super().__init__(nombre, especie, edad, habitat)

        self.__tamano = tamano
        
        def informacion(self):
            pass

        def sonido(self):
            return "Barrito"