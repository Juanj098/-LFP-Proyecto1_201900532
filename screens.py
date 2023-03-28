import tkinter as tk
from tkinter import*
import os
from fileinput import filename
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Treeview
from main import operar_, instruccion
from operaciones import Datos_O
from operacionestri import datatri
from operaciones import list_operaciones_
from main import instrucciones
from main import list_lexemas
from main import Data_gr
from reservadas import colors,formas
import webbrowser
from error import list_error
class Home(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(bg ='#404754')
        self.controller = controller
        self.init_widgets()


    def init_widgets(self):
        tk.Label(
            self,
            text = 'Proyecto no.1',
            justify = tk.CENTER,
            font = ('Jetbrains mono',16),
            bg='#404754'
            ).pack(
                side=tk.TOP,
                fill=tk.BOTH,
                expand= True,
                padx=22,
                pady=11
            )
#-> Izq
        optionsFrame_Izq = tk.Frame(self)
        optionsFrame_Izq.configure(
            bg='#404754',
            # width=200
        )
        optionsFrame_Izq.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx = 10,
            pady=11
        )
        btn1 = tk.Button(
                optionsFrame_Izq,
                text='Abrir',
                font=('Jetbrains mono',10),
                width=20,
                height=2,
                command=self.openFile
            )
        btn1.grid(row=1,column=0,padx=3,pady=3)
        btn2 = tk.Button(
            optionsFrame_Izq,
            text='Guardar',
            font=('Jetbrains mono',10),
            width=20,
            height=2,
            command=self.savaChange
        )
        btn2.grid(row =2,column=0,padx=3,pady=3)
        btn3 = tk.Button(
            optionsFrame_Izq,
            text='Analizar',
            font=('Jetbrains mono',10),
            width=20,
            height=2,
            command=self.analizar
        )
        btn3.grid(row=3,column=0,padx=3,pady=3)
        btn4 = tk.Button(
            optionsFrame_Izq,
            text='Errores',
            font=('Jetbrains mono',10),
            width=20,
            height=2,
            command=self.Errors
        )
        btn4.grid(row =4,column=0,padx=3,pady=3)
        lbl = tk.Label(
            optionsFrame_Izq,
            bg="#404754",
            text="AYUDA",
            font=('Jetbrains mono',10)
            )
        lbl.grid(row=5,column=0,padx=3,pady=4)
        btn5 = tk.Button(
            optionsFrame_Izq,
            text="Manual de usuario",
            font=('Jetbrains mono',10),
            width=20,
            height=1,
            command=self.Usuario
        )
        btn5.grid(row=6,column=0,padx=3,pady=3)
        btn6 = tk.Button(
            optionsFrame_Izq,
            text="Manual Tecnico",
            font=('Jetbrains mono',10),
            width=20,
            height=1,
            command=self.Tecnico
        )
        btn6.grid(row=7,column=0,padx=3,pady=3)
        btn7 = tk.Button(
            optionsFrame_Izq,
            text="Temas de Ayuda",
            font=("Jetbrains mono",10),
            width=20,
            height=1,
            command=self.Dev
        )
        btn7.grid(row=8, column=0,padx=3,pady=3)
        btn8 = tk.Button(
            optionsFrame_Izq,
            text="SALIR",
            font=('Jetbrains mono',10),
            width=20,
            height=2,
            command= self.quit
        )
        btn8.grid(row=9,column=0,padx=3,pady=3)

#-> der
        optionsFrame_Der = tk.Frame(self)

        optionsFrame_Der.configure(
            bg='#404754'
        )
        optionsFrame_Der.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx = 22,
            pady=11
        )
        self.Txt = tk.Text(
            optionsFrame_Der,
            font=('Jetbrains Mono',10),
            width=50,
            bg='#e5be77'
            )
        self.Txt.grid(row=1,column=1)

        self.txt_2 = tk.Text(
            optionsFrame_Der,
            font=('Jetbrains Mono',10),
            bg='#b6b5bd',
            width=100,
            state='disabled'
        )
        self.txt_2.grid(row=1,column=3,padx=3)

# -> functions

    def openFile(self):
        x = ''
        Tk().withdraw()
        try:
            self.filename = askopenfilename(
                title='Seleccione Archivo',
                filetypes=[('Archivos',f'*.json')]
                )
            with open(self.filename,encoding='UTF-8') as file:
                x = file.read()
        except:
            print('Error: No se selecciono ningun documento')
            return
        self.Insert(x)
        self.txt = x
        
    def Insert(self,txt):
        self.Txt.delete(1.0,tk.END)
        self.Txt.insert(1.0,txt)   
    
    def savaChange(self):
        try:
            mod = self.Txt.get(1.0,tk.END)
            with open(self.filename,'w+',encoding='UTF-8') as file:
                file.write(mod)
        except:
            print('Variable vacia')
            
    def analizar(self):
        list_lexemas.clear()
        instrucciones.clear()
        list_operaciones_.clear()

        txt = self.Txt.get(0.1,tk.END)

        instruccion(txt)
        resp = operar_()
        instruccion(txt)
        re = Data_gr()
        for r in resp:
            Data =Datos_O(r.getTipo(),r.getLeft(),r.getRight(),round(r.operar(None),3))
            list_operaciones_.append(Data)
        self.graficar(re.getTxt().getLexema(),re.getForma().getLexema(),re.getNodo().getLexema(),re.getFont().getLexema(),list_operaciones_)
        self.pdfGraph()
        self.txt_2.delete(1.0,tk.END)
        rr=''
        for l in list_operaciones_:
            rr +=f'{l.ret()}\n'
        self.txt_2.configure(state="normal")
        self.txt_2.delete(1.0,tk.END)
        self.txt_2.insert(1.0,rr)
        self.txt_2.configure(state="disabled")

    def Errors(self):
        list_error.clear()
        cadena = 'ERRORES_201900532\n'
        cadena +='{\n'
        txt = self.Txt.get(1.0,tk.END)
        instruccion(txt)
        cont = 0
        for err in list_error:
            if err != None:
                cadena+='\t{\n'
                cadena+=f'\t\t"No.":{str(cont)}\n'
                cadena+='\t\t"Descripcion-Token":{\n'
                cadena+=f'\t\t\t\t"Lexema":{err.geterror()}\n'
                cadena+=f'\t\t\t\t"Tipo":Error\n'
                cadena+=f'\t\t\t\t"Columna":{err.getCol()}\n'
                cadena+=f'\t\t\t\t"Fila":{err.getFila()}\n'
                cadena+='\t\t}\n'
                cadena+='\t},\n'
                cont = cont+1
        cadena+='}'
        print(cadena)
        self.txt_2.configure(state="normal")
        self.txt_2.delete(1.0,tk.END)
        self.txt_2.insert(1.0,cadena)
        self.txt_2.configure(state="disabled")
        
    def graficar(self,txt,figura,colorN,font,operaciones):
        for keys,value in colors.items():
            if colorN == keys:
                colorN = value
        for keys,value in colors.items():
            if font == keys:
                font = value
        for keys,value in formas.items():
            if figura == keys:
                figura = value
        cadena = '''
        digraph G{
            rankdir = LR
	        fontname="Helvetica,Arial,sans-serif"
	        node [fontname="Helvetica,Arial,sans-serif"]
            edge [fontname="Helvetica,Arial,sans-serif"]
        '''
        cadena += f'\tnode [shape = "{figura}" color = "{colorN}" style = filled fontcolor = "{font}"]\n'
        cadena+="\t\t\tsubgraph cluster0{\n"

        for x in range(len(operaciones)):
            cadena+= f'\t\t\t\tnodo{str(x+1)}[label=<<table><tr><td>{operaciones[x].getType()}</td></tr><tr><td>{operaciones[x].getResp()}</td></tr></table>>]\n'
            a=isinstance(operaciones[x].getLeft(),Datos_O)
            b=isinstance(operaciones[x].getLeft(),datatri)
            y=isinstance(operaciones[x].getRight(),Datos_O)
            z=isinstance(operaciones[x].getRight(),datatri)
            #izquierda trigonometrica o aritmetica
            if a == True:
                cadena+= f'\t\t\t\tnodoA{str(x+8)}[label=<<table><tr><td>{operaciones[x].getLeft().getType()}</td></tr><tr><td>{operaciones[x].getLeft().getResp()}</td></tr></table>>]\n'
                cadena+= f'\t\t\t\tnodoA{str(x+11)}[label="{operaciones[x].getLeft().getLeft()}"]\n'
                cadena+= f'\t\t\t\tnodoA{str(x+23)}[label="{operaciones[x].getLeft().getRight()}"]\n'
                cadena+= f'\t\t\t\tnodo{str(x+1)}->nodoA{str(x+8)}\n'
                cadena+= f'\t\t\t\tnodoA{str(x+8)}->nodoA{str(x+11)}\n'
                cadena+= f'\t\t\t\tnodoA{str(x+8)}->nodoA{str(x+23)}\n'

            elif b == True:
                cadena+= f'\t\t\t\tnodoB{str(x+8)}[label=<<table><tr><td>{operaciones[x].getLeft().getType()}</td></tr><tr><td>{operaciones[x].getLeft().getResp()}</td></tr></table>>]\n'
                cadena+= f'\t\t\t\tnodoB{str(x+11)}[label ="{operaciones[x].getLeft().getLeft()}"]\n'
                cadena+= f'\t\t\t\tnodo{str(x+1)}->nodoB{str(x+8)}\n'
                cadena+= f'\t\t\t\tnodoB{str(x+8)}->nodoB{str(x+11)}\n'
            else:
                cadena+= f'\t\t\t\tnodo{str(x+8)}[label="{operaciones[x].getLeft()}"]\n'
                cadena+= f'\t\t\t\tnodo{str(x+1)}->nodo{str(x+8)}\n'
            #derecha trigonometrica o aritmetica
            if y == True:
                cadena+= f'\t\t\t\tnodoY{str(x+16)}[label=<<table><tr><td>{operaciones[x].getRight().getType()}</td></tr><tr><td>{operaciones[x].getRight().getResp()}</td></tr></table>>]\n'
                cadena+= f'\t\t\t\tnodoY{str(x+19)}[label="{operaciones[x].getRight().getLeft()}"]\n'
                cadena+= f'\t\t\t\tnodoY{str(x+27)}[label="{operaciones[x].getRight().getRight()}"]\n'
                cadena+= f'\t\t\t\tnodo{str(x+1)}->nodoY{str(x+16)}\n'
                cadena+= f'\t\t\t\tnodoY{str(x+16)}->nodoY{str(x+19)}\n'
                cadena+= f'\t\t\t\tnodoY{str(x+16)}->nodoY{str(x+27)}\n'
            elif z == True:
                cadena+= f'\t\t\t\tnodoZ{str(x+16)}[label=<<table><tr><td>{operaciones[x].getRight().getType()}</td></tr><tr><td>{operaciones[x].getRight().getResp()}</td></tr></table>>]\n'
                cadena+= f'\t\t\t\tnodoZ{str(x+13)}[label="{operaciones[x].getRight().getLeft()}"]\n'
                cadena+= f'\t\t\t\tnodo{str(x+1)}->nodoZ{str(x+16)}\n'
                cadena+= f'\t\t\t\tnodoZ{str(x+16)}->nodoZ{str(x+13)}\n'
            else:
                cadena+= f'\t\t\t\tnodo{str(x+16)}[label="{operaciones[x].getRight()}"]\n'
                cadena+= f'\t\t\t\tnodo{str(x+1)}->nodo{str(x+16)}\n'

        cadena+="\t\t\t}\n"
        cadena += '}\n'

        with open('proyecto.dot','w',encoding="utf-8") as docu:
            docu.write(cadena)
            docu.close()
        os.system('dot -Tpdf proyecto.dot -o proyecto.pdf')
        

    def pdfGraph(self):
        path ='proyecto.pdf'
        webbrowser.open_new(path)
    
    def Usuario(self):
        path = 'Manual de usuario.pdf'
        webbrowser.open_new(path)

    def Tecnico(self):
        path = 'Manual Tecnico.pdf'
        webbrowser.open_new(path)
    
    def Dev(self):
        path = 'Datos.pdf'
        webbrowser.open_new(path)



        
class Proy(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(bg ='black')
        self.controller = controller
        
