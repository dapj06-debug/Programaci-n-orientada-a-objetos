# Tarea Semana 16 - Aplicación de Lista de Tareas

# Importamos la biblioteca tkinter para crear la interfaz gráfica de usuario y messagebox para mostrar mensajes emergentes
import tkinter as tk
from tkinter import messagebox

class Tareas:
    # Método constructor de la clase Tareas, que se ejecuta al crear una instancia de la clase
    def __init__(self, root):
        # Inicializamos la ventana principal de la aplicación, le damos un título y definimos su tamaño
        self.root = root
        self.root.title("APP TAREAS")
        self.root.geometry("500x550")

        #Label para el título de la aplicación        
        self.label_titulo = tk.Label(root, text="LISTA DE TAREAS", font=("Arial", 16, "bold"), pady=10)
        self.label_titulo.pack()

        # Frame para la entrada de nuevas tareas y el botón de añadir
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10, padx=20, fill="x")

        # Campo de entrada para escribir una nueva tarea
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # Agregamos un atajo de teclado para añadir la tarea al presionar Enter
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Botón para añadir la tarea a la lista
        btn_add = tk.Button(input_frame, text="Añadir", command=self.add_task, width=10)
        btn_add.pack(side="right")

        # Listbox para mostrar las tareas añadidas
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE, 
                                        activestyle="none", borderwidth=1)
        self.tasks_listbox.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Establecemos los atajos de teclado para completar y eliminar tareas
        self.tasks_listbox.bind("<c>", lambda event: self.complete_task())
        self.tasks_listbox.bind("<C>", lambda event: self.complete_task())
        self.tasks_listbox.bind("<Delete>", lambda event: self.delete_task())
        self.tasks_listbox.bind("<d>", lambda event: self.delete_task())
        self.tasks_listbox.bind("<D>", lambda event: self.delete_task())

        # Agregamos una barra de desplazamiento vertical al Listbox para manejar muchas tareas
        scrollbar = tk.Scrollbar(self.tasks_listbox)
        scrollbar.pack(side="right", fill="y")
        self.tasks_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tasks_listbox.yview)

        # Frame para los botones de completar y eliminar tareas
        button_frame = tk.Frame(root, pady=10)
        button_frame.pack(fill="x", padx=20)

        # Botón para marcar una tarea como completada
        self.btn_complete = tk.Button(button_frame, text="Completar (C)", command=self.complete_task, 
                                      width=15, bg="#4CAF50", fg="white")
        self.btn_complete.pack(side="left", padx=5)

        # Botón para eliminar una tarea de la lista
        self.btn_delete = tk.Button(button_frame, text="Eliminar (Supr)", command=self.delete_task, 
                                    width=15, bg="#f44336", fg="white")
        self.btn_delete.pack(side="right", padx=5)

        # Agregamos un atajo de teclado para cerrar la aplicación al presionar la tecla Escape
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    # Método para añadir una tarea a la lista
    def add_task(self):
        # Obtenemos el texto ingresado en el campo de entrada
        tarea = self.task_entry.get()
        if tarea.strip() != "":
            self.tasks_listbox.insert(tk.END, tarea)
            self.task_entry.delete(0, tk.END)
            # Regresar el foco a la entrada después de añadir
            self.task_entry.focus()
        else:
            messagebox.showwarning("Atención", "No puedes añadir una tarea vacía.")

    # Método para marcar una tarea como completada
    def complete_task(self, event=None):
        # Listbox para obtener la tarea seleccionada y marcarla como completada, cambiando su apariencia
        try:
            index = self.tasks_listbox.curselection()[0]
            tarea_actual = self.tasks_listbox.get(index)
            
            if "Completado" not in tarea_actual:
                nueva_tarea = f"{tarea_actual} (Completada)"
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, nueva_tarea)
                self.tasks_listbox.itemconfig(index, fg="gray", bg="#f9f9f9")
                
                self.tasks_listbox.selection_set(index)
        except IndexError:
            if not event: # Solo avisar si se usó el botón, no la tecla
                messagebox.showwarning("Selección", "Primero selecciona una tarea con el ratón.")

    # Método para eliminar una tarea de la lista
    def delete_task(self, event=None):
        # Listbox para obtener la tarea seleccionada y eliminarla de la lista
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            if not event:
                messagebox.showwarning("Selección", "Primero selecciona una tarea para eliminar.")

#Se crea la instancia de la aplicación y se inicia el bucle principal para mostrar la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = Tareas(root)
    root.mainloop()