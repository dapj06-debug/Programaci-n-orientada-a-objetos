# Tarea Semana 14 - Mi Agenda Personal

#importamos las bibliotecas necesarias para crear la interfaz gráfica de usuario y manejar fechas
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AgendaApp: 
    #Metodo constructor de la clase AgendaApp, que se ejecuta al crear una instancia de la clase
    def __init__(self, root):
        #Inicializamos la ventana principal de la aplicación, le damos un título y definimos su tamaño
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x700")

        # Creamos un marco principal para organizar los widgets dentro de la ventana
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(expand=True, fill="both")

        # Frame para la entrada de nuevos eventos
        input_frame = tk.LabelFrame(main_frame, text="Nuevo Evento", padx=10, pady=10)
        input_frame.pack(fill="x", pady=10)

        # Agregamos etiquetas y campos de entrada para la fecha, hora y descripción del evento
        tk.Label(input_frame, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0, sticky="w") #Etiqueta para el campo de fecha
        self.date_input = tk.Entry(input_frame, width=15) #Campo de entrada para la fecha del evento
        self.date_input.grid(row=0, column=1, padx=5, pady=5) #Establecemos la posición del campo de fecha en el grid del input_frame
       
        #Agregamos una etiqueta y un campo de entrada para la hora del evento       
        tk.Label(input_frame, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w", padx=(10, 0)) #Etiqueta para el campo de hora
        self.time_input = tk.Entry(input_frame, width=10) #Campo de entrada para la hora del evento
        self.time_input.grid(row=0, column=3, padx=5, pady=5) #Establecemos la posición del campo de hora en el grid del input_frame

        #Agregamos una etiqueta y un campo de entrada para la descripción del evento
        tk.Label(input_frame, text="Descripción:").grid(row=1, column=0, sticky="w") #Etiqueta para el campo de descripción
        self.desc_input = tk.Entry(input_frame, width=45) #Campo de entrada para la descripción del evento
        self.desc_input.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="we") #Establecemos la posición del campo de descripción en el grid del input_frame

        # Frame para la lista de eventos y los botones de acción
        list_frame = tk.Frame(main_frame) 
        list_frame.pack(expand=True, fill="both")  

        # Treeview para mostrar la lista de eventos con columnas para fecha, hora y descripción
        columns = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # Establecemos los encabezados de las columnas del Treeview
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")

        # Establecemos el ancho y la alineación de cada columna del Treeview
        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", width=300)
        
        self.tree.pack(side="left", expand=True, fill="both")

        # Scrollbar para el Treeview, para permitir desplazarse por la lista de eventos si hay muchos
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Frame para los botones de acción
        action_frame = tk.Frame(main_frame, pady=10)
        action_frame.pack(fill="x")

        # Agregamos botones para agregar, eliminar y salir de la aplicación, y los asociamos a sus respectivas funciones
        btn_add = tk.Button(action_frame, text="Agregar Evento", 
                            command=self.agregar_evento, bg="#4CAF50", fg="white", width=15)
        btn_add.pack(side="left", padx=5)
        btn_delete = tk.Button(action_frame, text="Eliminar Seleccionado", 
                               command=self.eliminar_evento, bg="#f44336", fg="white", width=20)
        btn_delete.pack(side="left", padx=5)
        btn_exit = tk.Button(action_frame, text="Salir", 
                             command=self.root.quit, width=10)
        btn_exit.pack(side="right", padx=5)

    #Función para agregar un evento
    def agregar_evento(self):
        fecha = self.date_input.get()
        hora = self.time_input.get()
        descripcion = self.desc_input.get()
        # Validación de que los campos no estén vacíos
        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            # Limpiamos los campos de entrada después de agregar el evento
            self.time_input.delete(0, tk.END)
            self.desc_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos (Fecha, Hora y Descripción).")

    #Función para eliminar un evento seleccionado
    def eliminar_evento(self):
        #Obtenemos el evento seleccionado en el Treeview
        selected_item = self.tree.selection()
        #Si hay un evento seleccionado, mostramos un mensaje de confirmación antes de eliminarlo
        if selected_item:
            confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if confirmar:
                for item in selected_item:
                    self.tree.delete(item)
        else:
            messagebox.showwarning("Atención", "Selecciona un evento de la lista para eliminarlo.")

# Se crea una instancia de la clase AgendaApp y se inicia el bucle principal de la aplicación para mostrar la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()