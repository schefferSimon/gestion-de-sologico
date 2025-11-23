from clases.claseAnimal import Animal

class Leon(Animal):
    def __init__(self, nombre, especie, edad, habitat, peso):
        super().__init__(nombre, especie, edad, habitat)

        if isinstance(peso, int) and not peso <= 0:
            self.__peso = peso
        else: raise TypeError("El peso otorgado no es valido o es menor a 1")
    
    def sonido(self):
        return "Rugido"

    