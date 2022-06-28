from tkinter import *
import tkinter as tk
from tkinter import ttk

class Matematicas_Menu(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        Label(parent, text="Menu de Matematicas").grid(row=0, column=0)

        ttk.Button(parent, text="Aritmetica", command=self.window).grid(row=1, column=0)

        ttk.Button(parent, text="Algebra", command=self.window).grid(row=2, column=0)

    def window(self):
        self.sw = Toplevel()
        Label(self.sw, text="Hello World").grid(row=0, column=0)
        

root = Tk()
root.title("Prueba de Mate")
Matematicas_Menu(root)
root.mainloop()