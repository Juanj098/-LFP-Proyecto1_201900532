from abs import *

class numeros(expression):
    
    def __init__(self, fila, columna, valor) -> None:
        self.valor = valor
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.valor
    
    def getCol(self):
        return super().getCol()
    
    def getFila(self):
        return super().getFila()
    
    def getNum(self):
        return self.valor
    
