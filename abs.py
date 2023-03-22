from abc import ABC,abstractmethod

class expression(ABC):

    def __init__(self,fila,columna) -> None:
        self.fila = fila
        self.columna = columna

    @abstractmethod
    def operar(self,arbol):
        pass

    @abstractmethod
    def getFila(self):
        self.fila

    @abstractmethod
    def getCol(self):
        return self.columna