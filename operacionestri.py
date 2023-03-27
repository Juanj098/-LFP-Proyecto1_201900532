class datatri:
    def __init__(self,left,tipo,res) -> None:
        self.left = left
        self.tipo = tipo
        self.res = res

    def getLeft(self):
        return self.left

    def getType(self):
        return self.tipo.getLexema()
    
    def getResp(self):
        return self.res
    
    def ret(self):
        return f'{self.opeS()}{self.left}), res -> {self.res}'
    
    def opeS(self):
        if self.tipo.getLexema() == 'Seno':
            return 'Sin('
        elif self.tipo.getLexema() == 'Tangente':
            return 'Tan('
        elif self.tipo.getLexema() == 'Coseno':
            return 'Cos('