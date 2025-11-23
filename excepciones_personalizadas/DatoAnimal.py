import Exception

class DatoAnimalError(Exception):
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2