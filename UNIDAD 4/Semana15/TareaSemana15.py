# Tarea Semana 15 - Aplicación de Lista de Tareas

# Importamos la biblioteca tkinter para crear la interfaz gráfica de usuario y messagebox para mostrar mensajes emergentes
import tkinter as tk
from tkinter import messagebox
class Tareas: #Definimos la clase Tareas, que representa nuestra aplicación de lista de tareas
    
    # El método constructor de la clase, que se ejecuta al crear una instancia de la clase
    def __init__(self, root):
        self.root = root
        self.root.title("APP TAREAS")
        self.root.geometry("500x500")

        # Configuración de la interfaz gráfica de usuario
        # Etiqueta del título de la aplicación
        self.label_titulo = tk.Label(root, text="LISTA DE TAREAS", font=("Arial", 16, "bold"), pady=10)
        self.label_titulo.pack()

        # Frame para el campo de entrada y el botón de añadir
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10, padx=20, fill="x")

        # Campo de entrada para escribir la tarea
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # Evento para añadir tarea al presionar Enter
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Botón para añadir la tarea a la lista
        btn_add = tk.Button(input_frame, text="Añadir", command=self.add_task, width=10)
        btn_add.pack(side="right")

        # Listbox para mostrar las tareas añadidas
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE, 
                                        activestyle="none", borderwidth=1)
        self.tasks_listbox.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Evento para completar tarea al hacer doble clic
        self.tasks_listbox.bind("<Double-Button-1>", lambda event: self.complete_task())

        # Scrollbar para la lista de tareas
        scrollbar = tk.Scrollbar(self.tasks_listbox)
        scrollbar.pack(side="right", fill="y")
        self.tasks_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tasks_listbox.yview)

        # Frame para los botones de completar y eliminar
        button_frame = tk.Frame(root, pady=10)
        button_frame.pack(fill="x", padx=20)

        # BOTÓN COMPLETAR (Verde)
        self.btn_complete = tk.Button(button_frame, text="Completar", command=self.complete_task, 
                                      width=15, bg="#4CAF50", fg="white")
        self.btn_complete.pack(side="left", padx=5)

        # BOTÓN ELIMINAR (Rojo)
        self.btn_delete = tk.Button(button_frame, text="Eliminar", command=self.delete_task, 
                                    width=15, bg="#f44336", fg="white")
        self.btn_delete.pack(side="right", padx=5)

    # Método para añadir una tarea a la lista
    def add_task(self):
        # Obtenemos el texto ingresado en el campo de entrada
        tarea = self.task_entry.get()
        if tarea.strip() != "":
            self.tasks_listbox.insert(tk.END, tarea)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "No puedes añadir una tarea vacía.")

    # Método para marcar una tarea como completada
    def complete_task(self):
        # Obtenemos el índice de la tarea seleccionada en el Listbox
        try:
            index = self.tasks_listbox.curselection()[0]
            tarea_actual = self.tasks_listbox.get(index)
            
            # Se verifica si la tarea ya está marcada como completada
            if "(Completada)" not in tarea_actual:
                nueva_tarea = f"{tarea_actual} (Completada)"
                
                # Se actualiza la tarea en el Listbox con el nuevo texto que indica que está completada
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, nueva_tarea)
                
                # Se cambia el color de la tarea a gris para indicar que está completada
                self.tasks_listbox.itemconfig(index, fg="gray")
                
        except IndexError:
            messagebox.showwarning("Selección", "Por favor, selecciona una tarea para completar.")
   
    # Método para eliminar una tarea de la lista
    def delete_task(self):
        # Obtenemos el índice de la tarea seleccionada en el Listbox y la eliminamos
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Selección", "Selecciona la tarea que deseas eliminar.")

# Se crea una instancia de la clase Tareas y se inicia el bucle principal de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Tareas(root)
    root.mainloop()