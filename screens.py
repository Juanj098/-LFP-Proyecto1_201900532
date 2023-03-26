import tkinter as tk
import os
from fileinput import filename
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.tix import Tree 
from main import operar_, instruccion
from operaciones import Datos_O
from operacionestri import datatri
from operaciones import list_operaciones_
from main import instrucciones
from main import list_lexemas
from main import Data_gr
from Data_g import grafica
from reservadas import colors,formas

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
            bg='#404754'
        )
        optionsFrame_Izq.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx = 22,
            pady=11
        )
        btn1 = tk.Button(
                optionsFrame_Izq,
                text='Abrir',
                font=('Jetbrains mono',10),
                width=15,
                height=2,
                command=self.openFile
            )
        btn1.grid(row=1,column=0,padx=3,pady=3)
        btn2 = tk.Button(
            optionsFrame_Izq,
            text='Guardar',
            font=('Jetbrains mono',10),
            width=15,
            height=2,
            command=self.savaChange
        )
        btn2.grid(row =2,column=0,padx=3,pady=3)
        btn3 = tk.Button(
            optionsFrame_Izq,
            text='Analizar',
            font=('Jetbrains mono',10),
            width=15,
            height=2,
            command=self.analizar
        )
        btn3.grid(row=3,column=0,padx=3,pady=3)
        btn4 = tk.Button(
            optionsFrame_Izq,
            text='Errores',
            font=('Jetbrains mono',10),
            width=15,
            height=2
        )
        btn4.grid(row =4,column=0,padx=3,pady=3)
        btn8 = tk.Button(
            optionsFrame_Izq,
            text="SALIR",
            font=('Jetbrains mono',10),
            width=15,
            height=2,
            command= self.quit
        )
        btn8.grid(row=8,column=0,padx=3,pady=3)

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
            bg='#e5be77'
            )
        self.Txt.grid(row=1,column=6)

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
        print(x)
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
        for l in list_operaciones_:
            print(f'->> {l.ret()}')


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
            rankdir = TB
	        fontname="Helvetica,Arial,sans-serif"
	        node [fontname="Helvetica,Arial,sans-serif"]
            edge [fontname="Helvetica,Arial,sans-serif"]
        '''
        cadena += f'\tnode [shape = "{figura}" color = "{colorN}" style = filled fontcolor = "{font}"]\n'
        for x in range(len(operaciones)):
            cadena+= f'\t\t\tsubgraph cluster{str(x)}'
            cadena+="{\n"
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
            elif b == True:
                cadena+= f'\t\t\t\tnodoB{str(x+8)}[label=<<table><tr><td>{operaciones[x].getLeft().getType()}</td></tr><tr><td>{operaciones[x].getLeft().getResp()}</td></tr></table>>]\n'
                cadena+= f'\t\t\t\tnodoB{str(x+11)}[label ="{operaciones[x].getLeft().getLeft()}"]\n'
            else:
                cadena+= f'\t\t\t\tnodo{str(x+8)}[label="{operaciones[x].getLeft()}"]\n'
            #derecha trigonometrica o aritmetica
            if y == True:
                cadena+= f'\t\t\t\tnodoY{str(x+16)}[label=<<table><tr><td>{operaciones[x].getRight().getType()}</td></tr><tr><td>{operaciones[x].getRight().getResp()}</td></tr></table>>]\n'
                cadena+= f'\t\t\t\tnodoY{str(x+19)}[label="{operaciones[x].getRight().getLeft()}"]'
                cadena+= f'\t\t\t\tnodoY{str(x+27)}[label="{operaciones[x].getRight().getRight()}"]'
            elif z == True:
                cadena+= f'\t\t\t\tnodoZ{str(x+16)}[label=<<table><tr><td>{operaciones[x].getRight().getType()}</td></tr><tr><td>{operaciones[x].getRight().getResp()}</td></tr></table>>]\n'
                cadena+= f'\t\t\t\tnodoz{str(x+13)}[label="{operaciones[x].getRight().getLeft()}"]'
            else:
                cadena+= f'\t\t\t\tnodo{str(x+16)}[label="{operaciones[x].getRight()}"]\n'

            cadena+="\t\t\t}\n"

        cadena += '}\n'

        with open('proyecto.dot','w',encoding="utf-8") as docu:
            docu.write(cadena)
            docu.close()
        os.system('dot -Tpdf proyecto.dot -o proyecto.pdf')

             



        
class Proy(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(bg ='black')
        self.controller = controller
        
