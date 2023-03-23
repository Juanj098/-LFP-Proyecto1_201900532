import tkinter as tk
from fileinput import filename
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.tix import Tree 

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
            height=2
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
            

        
class Proy(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(bg ='black')
        self.controller = controller
        
