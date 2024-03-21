import tkinter


class Maquina:
    def _init_(self, ventana):
        self.ventana= ventana
        self.ventana.tittle("maquina expendedora")









ventana = tkinter.Tk()
maquina = Maquina(ventana)  
ventana.mainloop()