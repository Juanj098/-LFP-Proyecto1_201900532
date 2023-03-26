list_graph = []
class grafica:
    def __init__(self,Text,C_nodo,Font,Forma) -> None:
        self.txt = Text
        self.c_nodo = C_nodo
        self.font = Font
        self.forma = Forma

    def getTxt(self):
        return self.txt
    
    def getNodo(self):
        return self.c_nodo
    
    def getFont(self):
        return self.font
    
    def getForma(self):
        return self.forma