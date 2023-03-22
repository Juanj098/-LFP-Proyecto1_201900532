from abs import *

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