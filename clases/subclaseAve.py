from clases.claseAnimal import Animal

class Ave(Animal):
    def __init__(self, nombre, especie, edad, habitat, tipoAve):
        super().__init__(nombre, especie, edad, habitat)

        self.__tipoAve = tipoAve

    def informacion(self):
        pass

    def sonido(self):
        return "Canto"

    def mover(self):
        return "Vuela"