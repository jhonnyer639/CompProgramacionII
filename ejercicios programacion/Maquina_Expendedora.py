import tkinter as tk
from tkinter import ttk, messagebox

class Tipo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo}"

class Producto:
    def __init__(self, tipo, nombre, codigo):
        self.tipo = tipo
        self.nombre = nombre
        self.codigo = codigo
        self.disponible = None

    def comprar(self, codigo):
        if self.disponible:
            messagebox.showinfo("Error", f"El producto {self.nombre} no está disponible")
        else:
            self.disponible = codigo
            messagebox.showinfo("Éxito", f"El producto {self.nombre} está disponible")

Productos = [
    Producto(Tipo("Comida"), "margarita", 1),
    Producto(Tipo("Bebida"), "CocaCola", 2)
]

def comprar_producto():
    producto = Productos[Producto_combobox.current()]
    codigo = codigo_entry.get()
    producto.comprar(codigo)

def agregar_producto():
    nombre = nuevo_producto_entry.get()
    tipo = nuevo_tipo_nombre_entry.get()
    codigo = nuevo_codigo_entry.get()

    nuevo_tipo = Tipo(tipo)
    nuevo_producto = Producto(nuevo_tipo, nombre, codigo)
    Productos.append(nuevo_producto)

    Producto_combobox['values'] = [producto.nombre for producto in Productos]
    messagebox.showinfo("Éxito", "Producto agregado correctamente")

# Configurar interfaz gráfica
root = tk.Tk()
root.title("Máquina expendedora")

# Widgets
label_producto = tk.Label(root, text="Producto:")
label_producto.grid(row=0, column=0, padx=10, pady=5)
Producto_combobox = ttk.Combobox(root, values=[producto.nombre for producto in Productos])
Producto_combobox.grid(row=0, column=1, padx=10, pady=5)

label_codigo = tk.Label(root, text="Código:")
label_codigo.grid(row=1, column=0, padx=10, pady=5)
codigo_entry = tk.Entry(root)
codigo_entry.grid(row=1, column=1, padx=10, pady=5)

comprar_b = tk.Button(root, text="Comprar producto", command=comprar_producto)
comprar_b.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

# Widgets para agregar productos
nuevo_producto_label = tk.Label(root, text="Nuevo producto:")
nuevo_producto_label.grid(row=4, column=0, padx=10, pady=5)
nuevo_producto_entry = tk.Entry(root)
nuevo_producto_entry.grid(row=4, column=1, padx=10, pady=5)

nuevo_tipo_nombre_label = tk.Label(root, text="Nuevo tipo:")
nuevo_tipo_nombre_label.grid(row=5, column=0, padx=10, pady=5)
nuevo_tipo_nombre_entry = tk.Entry(root)
nuevo_tipo_nombre_entry.grid(row=5, column=1, padx=10, pady=5)

nuevo_codigo_label = tk.Label(root, text="Código:")
nuevo_codigo_label.grid(row=6, column=0, padx=10, pady=5)
nuevo_codigo_entry = tk.Entry(root)
nuevo_codigo_entry.grid(row=6, column=1, padx=10, pady=5)

agregar_producto_button = tk.Button(root, text="Agregar Producto", command=agregar_producto)
agregar_producto_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

root.mainloop()

#Alba Yadira Nova Siera
#Jhonnyer Yampier Fresneda Malaver