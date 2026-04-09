#Aplicación GUI Básica blok de tareas

import tkinter as tk #Importamos la biblioteca tkinter para crear la interfaz gráfica de usuario
from tkinter import messagebox #Importamos messagebox para mostrar mensajes emergentes

# Funciones de los botones
def agregar_tarea(): #Función para agregar una tarea a la lista
    tarea = entrada.get() #Obtenemos el texto ingresado en la entrada de texto
    if tarea:
        lista_tareas.insert(tk.END, tarea) 
        entrada.delete(0, tk.END)

#Función para eliminar la última tarea de la lista
def eliminar_tarea():
    lista_tareas.delete(tk.END)

# Creación de la ventana
#Creamos la ventana principal de la aplicación, le damos un título y definimos su tamaño
ventana = tk.Tk()
ventana.title("Bloc de Tareas")
ventana.geometry("400x400")

# Creación de botones
#Creamos dos botones, uno para agregar tareas y otro para eliminar tareas, y los asociamos a sus respectivas funciones
btn_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)
btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Creación de la entrada de texto
#Creamos una entrada de texto 
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Creación de la lista de tareas
#Creamos una lista de tareas utilizando Listbox
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

#Ejecucion de la aplicación
ventana.mainloop()

    