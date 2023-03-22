from abs import expression

class Lexema(expression):
    
    def __init__(self, fila, columna, lexema) -> None:
        self.lexema = lexema
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.lexema
    
    def getCol(self):
        return super().getCol()
    
    def getFila(self):
        return super().getFila()