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
            return f'Operacion {self.ope.getLexema()}, -> [{self.left.ret()}] {self.sim()} {self.right} ={self.resp}'
        elif x == False and y == True and a == False and b == False: # (num - arit)
            return f'Operacion {self.ope.getLexema()}, -> {self.left}  {self.sim()} [{self.right.ret()}] ={self.resp}'
        elif a ==True and b == False and x == False and y == False:  # (tri - num)
            return f'Operacion {self.ope.getLexema()}, -> [{self.left.ret()}] {self.sim()} {self.right} ={self.resp}'
        elif a == False and b == True and x == False and y == False: # (num - tri)
            return f'Operacion {self.ope.getLexema()}, -> {self.left} {self.sim()} [{self.right.ret()}] ={self.resp}'
        elif a == True and b == True and x == False and y == False:  # (tri - tri)
            return f'Operacion {self.ope.getLexema()}, -> [{self.left.ret()}] {self.sim()} [{self.right.ret()}] ={self.resp}'        
        elif x == True and y == True and a == False and b == False:  # (arit - arit)
            return f'Operacion {self.ope.getLexema()}, -> [{self.left.ret()}] {self.sim()} [{self.right.ret()}] ={self.resp}'  
        elif x == True and b == True and a == False and y == False:  # (arit - tri)
            return f'Operacion {self.ope.getLexema()}, -> [{self.left.ret()}] {self.sim()} [{self.right.ret()}] ={self.resp}'
        elif a == True and y == True and b == False and x == False:  # (tri - arit)
            return f'Operacion {self.ope.getLexema()}, -> [{self.left.ret()}] {self.sim()} [{self.right.ret()}] ={self.resp}'  
        else: # (num - num)
            return f'Operacion {self.ope.getLexema()}, -> {self.left} {self.sim()} {self.right} = {self.resp}'

    def sim(self):
        if self.ope.getLexema() =='Suma':
            return '+'
        elif self.ope.getLexema() == 'Resta':
            return '-'
        elif self.ope.getLexema() == 'Multiplicacion':
            return '*'
        elif self.ope.getLexema() == 'Division':
            return '/'
        elif self.ope.getLexema() == 'Potencia':
            return '^'
        elif self.ope.getLexema() == 'Raiz':
            return '^ 1/'
        elif self.ope.getLexema() == 'Modulo':
            return '%'
        else:
            return self.ope.getLexema()


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