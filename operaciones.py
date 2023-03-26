list_operaciones_=[]
from operacionestri import datatri
class Datos_O:
    def __init__(self,operacion,Left,Right,resp) -> None:
        self.ope = operacion
        self.left = Left
        self.right = Right
        self.resp = resp
    
    def ret(self):
        x = isinstance(self.left,Datos_O) #->> arit
        y = isinstance(self.right,Datos_O) 
        a = isinstance(self.left,datatri) # ->> tri
        b = isinstance(self.right,datatri)

        if x == True and y == False:   # (arit - num)
            return f'tipo -> {self.ope.getLexema()} izq -> [{self.left.ret()}], der -> {self.right}, resp -> {self.resp}'
        elif x == False and y == True: # (num - arit)
            return f'tipo -> {self.ope.getLexema()} izq -> {self.left}, der -> [{self.right.ret()}], resp -> {self.resp}'
        elif a ==True and b == False:  # (tri - num)
            return f'tipo -> {self.ope.getLexema()} izq -> [{self.left.ret()}], der -> {self.right}, resp -> {self.resp}'
        elif a == False and b == True: # (num - tri)
            return f'tipo -> {self.ope.getLexema()} izq -> {self.left}, der -> [{self.right.ret()}], resp -> {self.resp}'
        elif a == True and b == True:  # (tri - tri)
            return f'tipo -> {self.ope.getLexema()} izq -> [{self.left.ret()}], der -> [{self.right.ret()}], resp -> {self.resp}'        
        elif x == True and y == True:  # (arit - arit)
            return f'tipo -> {self.ope.getLexema()} izq -> [{self.left.ret()}], der -> [{self.right.ret()}], resp -> {self.resp}'  
        elif x == True and a == True:  # (arit - tri)
            return f'tipo -> {self.ope.getLexema()} izq -> [{self.left.ret()}], der -> [{self.right.ret()}], resp -> {self.resp}'
        elif x == True and b == True:  # (tri - arit)
            return f'tipo -> {self.ope.getLexema()} izq -> [{self.left.ret()}], der -> [{self.right.ret()}], resp -> {self.resp}'  
        else: # (num - num)
            return f'tipo -> {self.ope.getLexema()} izq -> {self.left}, der -> {self.right}, resp -> {self.resp}'

    def getType(self):
        return self.ope.getLexema()
    
    def getResp(self):
        return self.resp
    
    def getLeft(self):
        x=isinstance(self.left,datatri)
        y=isinstance(self.left,Datos_O)
        return self.left

    def getRight(self):
        return self.right