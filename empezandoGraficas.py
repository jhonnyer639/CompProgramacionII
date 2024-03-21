import tkinter

def saludo(num1,num2):
    print("hola progeamadores")
    print(num1*num2)

def numerosCaja():
    numero1=int(cajaTexto.get())
    numero2=int(cajaTexto1.get())
    resultMultipl=numero1*numero2
    etiqueta2["text"]="el resultaod es: ",resultMultipl
ventana = tkinter.Tk()
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana, text="hola mundo",bg="green")
etiqueta.pack()

cajaTexto = tkinter.Entry(ventana, font="helveltica 20")
cajaTexto.pack()
cajaTexto1 = tkinter.Entry(ventana, font="arial 20")
cajaTexto1.pack()

boton = tkinter.Button(ventana,text="multiplicar", command=numerosCaja)
boton.pack()

etiqueta2 = tkinter.Label(ventana, text="")
etiqueta2.pack()
ventana.mainloop()

