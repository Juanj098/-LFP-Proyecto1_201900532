list_operaciones=[]

class Datos_O:
    def __init__(self,operacion,Left,Right,resp) -> None:
        self.ope = operacion
        self.left = Left
        self.right = Right
        self.resp = resp
    
    def ret(self):
        x = isinstance(self.left,Datos_O)
        y = isinstance(self.right,Datos_O)

        if x == True:
            return f'tipo -> {self.ope.getLexema()} izq -> [{self.left.ret()}], der -> {self.right}, resp -> {self.resp}'
        elif y == True:
            return f'tipo -> {self.ope.getLexema()} izq -> {self.left}, der -> [{self.right.ret()}], resp -> {self.resp}'
        elif y == True and x == True:
            return f'tipo -> {self.ope.getLexema()} izq -> [{self.left.ret()}], der -> [{self.right.ret()}], resp -> {self.resp}'
        else:
            return f'tipo -> {self.ope.getLexema()} izq -> {self.left}, der -> {self.right}, resp -> {self.resp}'

            



    def reet(self):
        pass
