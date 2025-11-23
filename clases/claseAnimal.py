class Animal():
    def __init__(self, nombre, especie, edad, habitat):
        if isinstance(nombre, str) and not nombre == "":
            self.__nombre = nombre
        else: raise TypeError("El nombre otorgado no es valido o esta vacio.")
        
        if isinstance(edad, int) and not edad <= 0:
            self.__edad = edad
        else: raise TypeError("El nombre otorgado no es valido o es menor a 1")
        
        if isinstance(habitat, str) and not habitat == "":
            self.__habitat = habitat
        else: raise TypeError("El habitat otorgado no es valido o esta vacio.")
        
        self.__especie = especie
    
    
    def getNombre(self):
        return f"{self.__nombre}"
    def getEspecie(self):
        return f"{self.__especie}"
    def getEdad(self):
        return f"{self.__edad}"
    def getHabitat(self):
        return f"{self.__habitat}"


    def informacion(self):
        return f"Nombre: {self.getNombre()}. Especie: {self.getEspecie()}. Edad: {self.getEdad()}. Habitat: {self.getHabitat()}. "
    
    def sonido(self):
        pass

    def alimentar(self, comida):
        pass

    def mover(self, *args): #Sobrecarga
        pass

    def camina(self):
        pass

    def camina(self, metros):
        pass

    