from clases.claseAnimal import Animal

class Elefante(Animal):
    def __init__(self, nombre, especie, edad, habitat, tamano):
        super().__init__(nombre, especie, edad, habitat)

        self.__tamano = tamano
        
    def informacion(self):
        return f"{super().informacion()} Tanaño: {self.__tamano}."

    def sonido(self):
        return "Barrito"