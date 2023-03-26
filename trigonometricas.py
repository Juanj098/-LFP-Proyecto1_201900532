from abs import *
from math import * 
from numeros import numeros
from operacionestri import datatri

class Trigonometrica(expression):

    def __init__(self, left, tipo, fila, columna) -> None:
        self.left = left
        self.tipo = tipo
        super().__init__(fila, columna)
    
    def operar(self, arbol):
        leftValue = ''
        if self.left != None:
            leftValue = self.left.operar(arbol)
        if self.tipo.operar(arbol) == 'Seno':
            return sin(leftValue)
        elif self.tipo.operar(arbol) == 'Coseno':
            return cos(leftValue)
        elif self.tipo.operar(arbol) == 'Tangente':
            return tan(leftValue)
        else:
            return 0
    
    def getCol(self):
        return super().getCol()
    
    def getFila(self):
        return super().getFila()
    
    def getNum(self):
        x = isinstance(self.left,numeros)
        if x == True:
            return self.left.getNum()
        else:
            return self.left
    
    def getTipo(self):
        return self.tipo