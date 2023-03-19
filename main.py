from reservadas import reserv

doc = 'datos.json'

lexemas = list(reserv.values())

global n_lineas
global n_col
global instrucciones
global list_lexemas

n_lineas = 1
n_col = 1
list_lexemas = []

def instruccion(cadena):
    global n_lineas
    global n_col
    global list_lexemas
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
                # se agrega a lista de lexemas
                list_lexemas.append(lexema)
                n_col += len(lexema)+1
                puntero = 0
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
            cadena = cadena[1:]
            puntero = 0
            n_col += 1

    for lex in list_lexemas:
        print(lex)

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


# with open('datos.json','r') as file:
#     cont = file.readlines()
cont = '''{
    {
        "Operacion":"Suma" 
        "Valor1":4.5 
        "Valor2":5.32
    }, 
    {
        "Operacion":"Resta" 
        "Valor1":4.5 "Valor2": [ 
            "Operacion":"Potencia" 
            "Valor1":10 
            "Valor2":3
    ]}, 
    {
        "Operacion":"Suma" 
        "Valor1":[ 
            "Operacion":"Seno" 
            "Valor1":90
        ] 
        "Valor2":5.32 
    }
    "Texto":"Realizacion de Operaciones" 
    "Color-Fondo-Nodo":"Amarillo" 
    "Color-Fuente-Nodo":"Rojo"
    "Forma-Nodo":"Circulo"
}'''


instruccion(cont)
