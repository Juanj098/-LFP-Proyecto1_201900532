from abs import expression

list_error = []

class Errores():
    def __init__(self, fila, columna, errores) -> None:
        self.error = errores
        self.fila = fila
        self.col = columna

    def getCol(self):
        return self.col
    
    def getFila(self):
        return self.fila

    def geterror(self):
        return self.error
    
 