from abs import *
from numeros import numeros
from operaciones import Datos_O
from trigonometricas import Trigonometrica
from operacionestri import datatri

class Aritmetica(expression):
    
    def __init__(self, izq,der,tipo,fila,columna) -> None:
        self.izq = izq
        self.der = der
        self.tipo = tipo
        super().__init__(fila, columna)
  
    def operar(self, arbol):
        rightValue = ''
        leftValue = ''
        if self.izq != None:
            leftValue = self.izq.operar(arbol)
        if self.der != None:
            rightValue = self.der.operar(arbol)

        if self.tipo.operar(arbol) == 'Suma':
            return leftValue + rightValue
        elif self.tipo.operar(arbol) == 'Resta':
            return leftValue - rightValue
        elif self.tipo.operar(arbol) == 'Multiplicacion':
            return leftValue * rightValue
        elif self.tipo.operar(arbol) == 'Division':
            return leftValue/rightValue
        elif self.tipo.operar(arbol) =='Potencia':
            return leftValue**rightValue
        elif self.tipo.operar(arbol) == 'Modulo':
            return leftValue%rightValue
        elif self.tipo.operar(arbol) == "Raiz":
            return leftValue**(1/rightValue)
        elif self.tipo.operar(arbol) == 'Inverso':
            return (1/leftValue)
        else:
            return 0
    
    def getCol(self):
        return super().getCol()
    
    def getFila(self):
        return super().getFila()  
    
    def getLeft(self):
        if self.izq != None:
            x = isinstance(self.izq,numeros)
            y = isinstance(self.izq,Aritmetica)
            z = isinstance(self.izq,Trigonometrica)
            if x == True:
                return self.izq.getNum()
            elif y == True:
                return Datos_O(self.izq.getTipo(),self.izq.getLeft(),self.izq.getRight(),self.izq.operar(None))
            elif z == True:
                return datatri(self.izq.getNum(),self.izq.getTipo(),round(self.izq.operar(None),3))

        else:
            return None
        
    def getRight(self):
        if self.der != None:
            x = isinstance(self.der,numeros)
            y = isinstance(self.der,Aritmetica)
            z = isinstance(self.der,Trigonometrica)
            if x == True:
                return self.der.getNum()
            elif y == True:
                return Datos_O(self.der.getTipo(),self.der.getLeft(),self.der.getRight(),self.der.operar(None))
            elif z == True:
                return datatri(self.der.getNum(),self.der.getTipo(),round(self.der.operar(None),3))
        else:
            return None
    
    def getTipo(self):
        return self.tipo