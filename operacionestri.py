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
        return f'tipo -> {self.tipo.getLexema()}, izq -> {self.left}, res -> {self.res}'