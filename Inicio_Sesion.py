from tkinter import *
import tkinter as tk
from tkinter import ttk
import Base_Datos_Conexion as BDC
from tkinter import messagebox as mb



class Credenciales(ttk.Frame):

    def __init__(self, parent):
        self.main_window = parent
        self.main_window.title("Iniciar Sesion")
        self.main_window.configure(bg='white')
        self.main_window.resizable(0, 0)
        
        self.Conexion = BDC.Conexion_Base_Datos()
        self.login(parent)
        
        
    def login(self, root):

        self.frame = LabelFrame(root, text=None, padx=50, pady=50, bg="#fae5d3", border=0.9)
        self.frame.grid(row=0, column=0, padx=100, pady=100)

        Label(self.frame, text="Acceder a Social Network", justify="center").grid(
            row=0, column=0, columnspan=2, pady=5)

        Label(self.frame, text="Usuario:").grid(row=1, column=0, pady=5)
        self.User=StringVar()
        Entry(self.frame, textvariable=self.User).grid(row=1, column=1, pady=5)
            
        Label(self.frame, text="Contraseña:").grid(row=2, column=0, pady=5)
        self.Pass=StringVar()
        Entry(self.frame, textvariable=self.Pass, show="*").grid(row=2, column=1, pady=5)
        

        Button(self.frame, text="Iniciar Sesion", command=self.Verificacion).grid(
            row=5, column=0, columnspan=2, pady=5)
        
        Button(self.frame, text="Registrarse", command=self.Registro).grid(
            row=6, column=0, columnspan=2, pady=5)
        
        Button(self.frame, text="¿Olvidaste tu contraseña?", command=self.Olvido).grid(
            row=7,  column=0, columnspan=2, pady=5)

    def Verificacion(self):
        
        datos=(self.User.get(), self.Pass.get())
        #print(datos)
        retorno = self.Conexion.Conexion_User1(datos)
        if retorno == True:
            self.Sesion()
        else:
            #mb.showinfo(message="Contraseña o Usuario Incorrecto", title="Credenciales Incorrectas")
            Label(self.frame, text="Contraseña o Usuario Incorrecto").grid(
                row=4, column=0, columnspan=2)
    
    def Sesion(self):
        self.main_window.withdraw()
        self.win_sesion = Toplevel()
        
        Label(self.win_sesion, text="Hola 1").grid(row=0, column=0)

        if self.win_sesion.destroy() == True:
            self.main_window.deiconify()
    
    def Registro(self):
        
        self.win_registro = Toplevel()
        
        Label(self.win_registro, text="Hola 2").grid(row=0, column=0)

    def Olvido(self):
        
        self.win_olvido = Toplevel()
        
        Label(self.win_olvido, text="Hola 3").grid(row=0, column=0)

    

#root.geometry("400x300")
#root.minsize(400, 300)
if __name__ == "__main__":
    root = Tk()
    Credenciales(root)
    root.mainloop()
