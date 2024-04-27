from tkinter import ttk , messagebox
from tkinter import *
import tkinter as tk
import pyodbc

def nuevo():
    nombre = txt_nombre.get()
    apellido = txt_apellido.get()
    fecha_nac = txt_fecha.get()
    telefono = txt_telefono.get()
    correo = txt_correo.get()
    cargo = txt_cargo.get()
    salario = txt_salario.get()

    if nombre and apellido and fecha_nac and telefono and correo and cargo and salario:
        try:
            with conexion.cursor() as cur:
                sql = '''INSERT INTO Empleados (Nombre, Apellido, FechaNac, Telefono, Correo, Cargo, Salario) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)'''
                cur.execute(sql, (nombre, apellido, fecha_nac, telefono, correo, cargo, salario))
                conexion.commit()
                messagebox.showinfo("Éxito", "Empleado agregado exitosamente")
                limpiar_campos()
                llenar_datos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el empleado: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "Por favor complete todos los campos")

def modificar():
    seleccion = grid.focus()

    if seleccion:
        detalles_empleado = grid.item(seleccion)

        def guardar_modificaciones():
            nuevo_nombre = txt_nombre.get()
            nuevo_apellido = txt_apellido.get()
            nueva_fecha = txt_fecha.get()
            nuevo_telefono = txt_telefono.get()
            nuevo_correo = txt_correo.get()
            nuevo_cargo = txt_cargo.get()
            nuevo_salario = txt_salario.get()

            grid.item(seleccion, values=(nuevo_nombre, nuevo_apellido, nueva_fecha, nuevo_telefono, nuevo_correo, nuevo_cargo, nuevo_salario))
            ventana_modificar.destroy()

        ventana_modificar = tk.Toplevel()
        ventana_modificar.title("Alerta")

        nuevo_nombre_label = tk.Label(ventana_modificar, text="seguro que quiere modificar el empleado "+detalles_empleado['values'][0])
        nuevo_nombre_label.grid(row=0, column=0)


        guardar_button = tk.Button(ventana_modificar, text="Modificar", command=guardar_modificaciones)
        guardar_button.grid(row=8, columnspan=2)

    else:
        messagebox.showwarning("Advertencia", "Por favor seleccione un empleado para modificar")

def eliminar():
    seleccion = grid.focus()
    if seleccion:
        id_empleado = grid.item(seleccion)['text']
        try:
            with conexion.cursor() as cur:
                sql = "DELETE FROM Empleados WHERE Id = ?"
                cur.execute(sql, id_empleado)
                conexion.commit()
                messagebox.showinfo("Éxito", "Empleado eliminado exitosamente")
                llenar_datos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el empleado: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "Por favor seleccione un empleado")

def llenar_datos():
    grid.delete(*grid.get_children())
    try:
        with conexion.cursor() as cur:
            cur.execute("SELECT * FROM Empleados")
            datos = cur.fetchall()
            for row in datos:
                grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener los datos de los empleados: {str(e)}")

def limpiar_campos():
    txt_nombre.delete(0, tk.END)
    txt_apellido.delete(0, tk.END)
    txt_fecha.delete(0, tk.END)
    txt_telefono.delete(0, tk.END)
    txt_correo.delete(0, tk.END)
    txt_cargo.delete(0, tk.END)
    txt_salario.delete(0, tk.END)

def main():
    global conexion, txt_nombre, txt_apellido, txt_fecha, txt_telefono, txt_correo, txt_cargo, txt_salario, grid

    ventana = tk.Tk()
    ventana.title("Gestión de Empleados")
    ventana.state("zoomed")

    frame1 = tk.Frame(ventana, bg="#bfdaff")
    frame1.place(x=0, y=0, width=93, relheight=1)

    Bt_limpiar = tk.Button(frame1, text="Limpiar", command=limpiar_campos, bg="blue", fg="white")
    Bt_limpiar.place(x=5, y=80, width=80, height=30)

    Bt_modificar = tk.Button(frame1, text="Modificar", command=modificar, bg="blue", fg="white")
    Bt_modificar.place(x=5, y=125, width=80, height=30)

    Bt_eliminar = tk.Button(frame1, text="Eliminar", command=eliminar, bg="blue", fg="white")
    Bt_eliminar.place(x=5, y=165, width=80, height=30)

    frame2 = tk.Frame(ventana, bg="#d3dde3")
    frame2.place(x=95, y=0, width=150, relheight=1)

    lbl_nombre = tk.Label(frame2, text="Nombre: ", bg="#d3dde3")
    lbl_nombre.grid(row=0, column=0)
    txt_nombre = tk.Entry(frame2)
    txt_nombre.grid(row=1, column=0)

    lbl_apellido = tk.Label(frame2, text="Apellido: ", bg="#d3dde3")
    lbl_apellido.grid(row=2, column=0)
    txt_apellido = tk.Entry(frame2)
    txt_apellido.grid(row=3, column=0)

    lbl_fecha = tk.Label(frame2, text="Fecha de Nacimiento: ", bg="#d3dde3")
    lbl_fecha.grid(row=4, column=0)
    txt_fecha = tk.Entry(frame2)
    txt_fecha.grid(row=5, column=0)

    lbl_telefono = tk.Label(frame2, text="Teléfono: ", bg="#d3dde3")
    lbl_telefono.grid(row=6, column=0)
    txt_telefono = tk.Entry(frame2)
    txt_telefono.grid(row=7, column=0)

    lbl_correo = tk.Label(frame2, text="Correo: ", bg="#d3dde3")
    lbl_correo.grid(row=8, column=0)
    txt_correo = tk.Entry(frame2)
    txt_correo.grid(row=9, column=0)

    lbl_cargo = tk.Label(frame2, text="Cargo: ", bg="#d3dde3")
    lbl_cargo.grid(row=10, column=0)
    txt_cargo = tk.Entry(frame2)
    txt_cargo.grid(row=11, column=0)

    lbl_salario = tk.Label(frame2, text="Salario: ", bg="#d3dde3")
    lbl_salario.grid(row=12, column=0)
    txt_salario = tk.Entry(frame2)
    txt_salario.grid(row=13, column=0)

    bt_guardar = tk.Button(frame2, text="Guardar", command=nuevo, bg="green", fg="white")
    bt_guardar.grid(row=14, column=0, columnspan=1)

    lab = Label(frame1, text="conexion")
    lab.place(width=100, height=20)

    grid = ttk.Treeview(ventana, columns=("Nombre", "Apellido", "Fecha Nac.", "Teléfono", "Correo", "Cargo", "Salario"))
    grid.column("#0", width=20)
    grid.column("Teléfono", width=100)
    grid.column("Cargo", width=100)

    grid.heading("#0", text="ID")
    grid.heading("Nombre", text="Nombre")
    grid.heading("Apellido", text="Apellido")
    grid.heading("Fecha Nac.", text="Fecha de Nacimiento")
    grid.heading("Teléfono", text="Teléfono")
    grid.heading("Correo", text="Correo")
    grid.heading("Cargo", text="Cargo")
    grid.heading("Salario", text="Salario")
    grid.place(x=247, y=0, width=1150,height=700)

    try:
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};'
            'Server=KAKAROTTO639\SQLEXPRESS;'
            'DATABASE=Datos;'
            'Trusted_Connection=yes;'
        )
        llenar_datos()
        lab2 = Label(frame1,text="enabled",fg="green")
        lab2.place(y=20,width=100,height=20)
        
    except Exception as e:
        lab2 = Label(frame1,text="disable",fg="red")
        lab2.place(y=20,width=100,height=20)
    ventana.mainloop()

if __name__ == "__main__":
    main()

#Jhonnyer Yampier Fresneda Malaver
#Alaba Yadira nova Sierra