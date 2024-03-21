import tkinter
from tkinter import ttk, messagebox

class Bebida:
    def __init__(self, nombre):
        self.__nombre = nombre

    def getNombreBebida(self):
        return f"La bebida es {self.__nombre}"
    
class Producto:
    def __init__(self, costo, precio):
        self.costo = costo
        self.precio = precio
    
    def getGanancia(self):
        return f"la ganacia es: {self.precio - self.costo}"

class Cerveza(Bebida, Producto):

    __Count = 0

    def __init__(self, nombre, marca, alcohol, costo, precio):
        Bebida.__init__(self, nombre)
        Producto.__init__(self, costo, precio)
        self.__marca = marca
        self.__alcohol = alcohol
        Cerveza.__Count += 1
    
    def getNombreBebida(self):
        return f"{super().getNombreBebida()} de la marca {self.__marca} con grado de alchohol {self.__alcohol} grados"
    
    def saludarComensal(self, nombre, edad):

        if edad < 18:
            return f"Hola {nombre} tu edad es {edad} no debes berberme"
        else:
            return f"Hola {nombre} el exceso de alcohol es perjudicial para la salud"


    @staticmethod
    def getContadorDeCervezas():
        return f"se han creado {Cerveza.__Count} cervezas"
    
ventana = tkinter.Tk()
ventana.title("Maquina expendedora")
ventana.geometry("700x700")
ventana.columnconfigure(0,weight=2)
ventana.rowconfigure(0,weight=1)


etiqueta_pr2 = tkinter.Label(ventana, text="Margaritas")
etiqueta_pr2.grid(row=0, column=0)






cerveza = Cerveza("Poker", "Bavaria", 4.0, 1500, 2000)
cerveza2 = Cerveza("Aguila","Bavaria", 4.0, 1400, 2000)

ventana.mainloop()
# bedida = Bebida("Jugo de mora")
# print(bedida.getNombreBebida())
