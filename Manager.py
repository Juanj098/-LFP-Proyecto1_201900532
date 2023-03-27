import tkinter as tk
from tkinter import ttk
from screens import Home
from screens import Proy

class Window(tk.Tk):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.title('Proyecto no.1')
        self.geometry('1250x500')
        container = tk.Frame(self)
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True 
        )
        container.configure(bg = '#404754')
        container.grid_columnconfigure(0,weight = 1)
        container.grid_rowconfigure(1,weight = 1)

        self.frames = {}

        for F in (Home,Proy):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky=tk.NSEW)
        self.showFrame(Home)

    def showFrame(self,container):
        frame = self.frames[container]
        frame.tkraise()