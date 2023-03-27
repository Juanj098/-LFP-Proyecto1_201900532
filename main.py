from reservadas import reserv
from aritmeticas import *
from trigonometricas import *
from lexema import *
from numeros import *
from operaciones import Datos_O
from Data_g import grafica
from Data_g import list_graph
from error import Errores
from error import list_error
doc = 'datos.json'
lexemas = list(reserv.values())


global n_lineas
global n_col
global instrucciones
global list_lexemas

n_lineas = 1
n_col = 1
instrucciones = []
list_lexemas = []
list_errores = []
def instruccion(cadena):
    global n_lineas
    global n_col
    global list_lexemas
    global list_errores
    lexema = ''
    puntero = 0

    while cadena:
        char = cadena[puntero]
        puntero += 1
        if char == '\"':
            lexema, cadena = armar_lex(cadena[puntero:])
            if lexema and cadena:
                n_col+=1
                # armo lexema como clase
                l = Lexema(n_lineas,n_col,lexema)
                # se agrega a lista de lexemas
                list_lexemas.append(l)
                n_col += len(lexema)+1
                puntero = 0
        elif char.isdigit():
            token, cadena = armar_no(cadena)
            if token and cadena:
                n_col += 1
                #numero como clase
                n = numeros(n_lineas,n_col,token)
                list_lexemas.append(n)
                n_col += len(str(token))+1
                puntero = 0
        elif char == '[' or char == ']':
            #se arma lexema como clase
            ch = Lexema(n_lineas,n_col,char)
            list_lexemas.append(ch)
            cadena = cadena[1:]
            puntero = 0
            n_col += 1
        elif char == '\t':
            n_col += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_lineas += 1
            n_col = 1
        else:
            #for key, value in reserv.items():
            #   if char != value:
            if char != "{" and char != "}" and char != "[" and char != "]" and char != ":" and char != "," and char != "." and char != '\t' and char != ' ':
                er = Errores(n_lineas,n_col,char)
                list_error.append(er)
            cadena = cadena[1:]
            puntero = 0
            n_col += 1
    
    return list_lexemas

def armar_no(cadena):
    token = ''
    puntero = ''
    is_dec = False
    for char in cadena:
        puntero += char
        if char == '.':
            is_dec = True
        if char == '\"' or char == ' ' or char == '\t' or char == '\n':
            if is_dec == True:
                return float(token), cadena[len(puntero)-1:]
            else:
                return int(token), cadena[len(puntero)-1:]
        else:
            token += char
    return None, None

def armar_lex(cadena):
    global n_lineas
    global n_col
    global list_lexemas
    lexema = ''
    puntero = ''
    for char in cadena:   
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None

def operar():
    global list_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    while list_lexemas:
        lexema = list_lexemas.pop(0)
        if lexema.operar(None) == 'Operacion':
            operacion = list_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = list_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = list_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()
        
        if operacion and n1 and n2:
            return Aritmetica(n1, n2, operacion,f'Inicio:{operacion.getFila()}:{operacion.getCol()}',f'fin:{n2.getFila()}:{n2.getCol()}')
        elif operacion and n1 and operacion.operar(None) == 'Seno' or operacion and n1 and operacion.operar(None) =='Coseno' or operacion and n1 and operacion.operar(None) =='Tangente':
            return Trigonometrica(n1, operacion,f'Inicio:{operacion.getFila()}:{operacion.getCol()}',f'Fin:{n1.getFila()}:{n1.getCol()}')
    return None

def operar_():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    return instrucciones

def Data_gr():
    global list_lexemas
    global instrucciones
    txt = ''
    font =''
    c_nodo =''
    forma =''
    while list_lexemas:
        lexema =list_lexemas.pop(0)
        if lexema.operar(None) == 'Texto':
            txt = list_lexemas.pop(0)
        elif lexema.operar(None) == 'Color-Fondo-Nodo':
            c_nodo = list_lexemas.pop(0)
        elif lexema.operar(None) == 'Color-Fuente-Nodo':
            font = list_lexemas.pop(0)
        elif lexema.operar(None) == 'Forma-Nodo':
            forma = list_lexemas.pop(0)
        if txt and font and c_nodo and forma:
            return grafica(txt,c_nodo,font,forma)    
    return None


cont = '''{
    { ?
    {
        "Operacion":"Resta"
        "Valor1":6.5
        "Valor2":3.5
    }, *
    {
        "Operacion":"Multiplicacion" ^
        "Valor1":[
            "Operacion":"Seno"
            "Valor1":2
        ]
        "Valor2": [
            "Operacion":"Potencia"
            "Valor1":2
            "Valor2":2
        ] +
    },
    {
        "Operacion":"Suma"
        "Valor1":[
        "Operacion":"Seno"
        "Valor1":90
        ]
        "Valor2":5.32
    },
    { ! $ %@
        "Operacion":"Resta"
        "Valor1": [
            "Operacion": "Division"
            "Valor1": 500
            "Valor2": 100
        ]
        "Valor2": [
            "Operacion": "Multiplicacion"
            "Valor1": 10
            "Valor2": 15
     ]},
    "Texto":"Realizacion de Operaciones"
    "Color-Fondo-Nodo":"Amarillo"
    "Color-Fuente-Nodo":"Rojo"
    "Forma-Nodo":"Circulo"
    @
}
    '''



