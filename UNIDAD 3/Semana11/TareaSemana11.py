# Sistema de Gestión de Inventario

import os # Importamos os para manejo de archivos y verificación de existencia

class Producto: 
    # metodo constructor para inicializar los atributos del producto
    def __init__(self, ID, nombre, cantidad, precio):
        self._ID = ID
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters para cada atributo
    def get_ID(self): return self._ID
    def get_nombre(self): return self._nombre
    def set_nombre(self, nombre): self._nombre = nombre
    def get_cantidad(self): return self._cantidad
    def set_cantidad(self, cantidad): self._cantidad = cantidad
    def get_precio(self): return self._precio
    def set_precio(self, precio): self._precio = precio
    def __str__(self):
        return f"ID: {self._ID:<10} | Nombre: {self._nombre:<20} | Stock: {self._cantidad:<5} | Precio: ${self._precio:.2f}"

# Clase Inventario con Colección de Diccionario
class Inventario:
    # metodo constructor para inicializar el inventario y cargar datos desde un archivo
    def __init__(self, archivo="inventario.txt"):
        # Usamos un diccionario para búsqueda rápida por ID
        self.productos = {} #usamos {} para crear un diccionario
        self.archivo = archivo
        self.cargar_desde_archivo()

    # Método para cargar productos desde un archivo de texto
    def cargar_desde_archivo(self):
        #usamos if y os.path.exists para verificar si el archivo existe antes de intentar cargarlo
        if not os.path.exists(self.archivo):
            return
        #usamos try-except para manejar posibles errores al leer el archivo
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split('|')
                    if len(partes) == 4:
                        ID, nombre, cantidad, precio = partes
                        # Al cargar, insertamos en el diccionario
                        self.productos[ID] = Producto(ID, nombre, int(cantidad), float(precio))
        except (FileNotFoundError, PermissionError, ValueError) as e:
            print(f"Aviso: No se pudo cargar el archivo correctamente ({e})")

# Metodo para guardar productos en un archivo de texto
    def guardar_en_archivo(self):
        #usamos try-except para manejar posibles errores al escribir en el archivo
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for p in self.productos.values():
                    f.write(f"{p.get_ID()}|{p.get_nombre()}|{p.get_cantidad()}|{p.get_precio()}\n")
            return True
        except PermissionError:
            print("Error: Permisos insuficientes para guardar.")
            return False
        
# Métodos para añadir producto 
    def añadir_producto(self, producto):
        #if para verificar si el ID del producto ya existe en el inventario y evitar duplicados
        if producto.get_ID() in self.productos:
            return False, "Error: El ID ya existe en el inventario."
        
        #Se añade el producto al diccionario usando su ID como clave para acceso rápido
        self.productos[producto.get_ID()] = producto
        if self.guardar_en_archivo():
            return True, "Producto añadido y guardado exitosamente."
        else:
            return False, "Error: No se pudo guardar el producto en el archivo."    

# Método para eliminar un producto por su ID 
    def eliminar_producto(self, ID):
        #if para verificar la existencia del producto
        if ID in self.productos:
            del self.productos[ID]
            self.guardar_en_archivo()
            return True, "Producto eliminado correctamente."
        return False, "Error: Producto no encontrado."

# Método para actualizar la cantidad y/o precio de un producto
    def actualizar_producto(self, ID, cantidad=None, precio=None):
        #if para verificar la existencia del producto antes de intentar actualizarlo
        if ID in self.productos:
            #if para actualizar la cantidad y el precio
            if cantidad is not None:
                self.productos[ID].set_cantidad(cantidad)
            if precio is not None:
                self.productos[ID].set_precio(precio)
            self.guardar_en_archivo()
            return True, "Producto actualizado correctamente."
        return False, "Error: Producto no encontrado."

# Método para buscar productos por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        return encontrados

# Método para obtener todos los productos en el inventario
    def obtener_todos(self):
        return list(self.productos.values())

# Interfaz de Usuario
def mostrar_menu():
    inv = Inventario()
    while True:
        print("\n SISTEMA DE GESTIÓN DE INVENTARIO")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto (Cantidad/Precio)")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Inventario Completo")
        print("6. Salir")

        op = input("Seleccione una opción: ").strip()

        if op == '1':
            idx = input("ID único: ")
            nom = input("Nombre: ")
            try:
                can = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                status, msg = inv.añadir_producto(Producto(idx, nom, can, pre))
                print(msg)
            except ValueError:
                print("Dato inválido. Cantidad debe ser entero y precio numérico.")

        elif op == '2':
            idx = input("ID del producto a eliminar: ")
            status, msg = inv.eliminar_producto(idx)
            print(msg)

        elif op == '3':
            idx = input("ID del producto a actualizar: ")
            if idx in inv.productos:
                print("Deje en blanco si no desea cambiar el valor.")
                can_in = input("Nueva cantidad: ")
                pre_in = input("Nuevo precio: ")

                nueva_can = int(can_in) if can_in else None
                nuevo_pre = float(pre_in) if pre_in else None

                status, msg = inv.actualizar_producto(idx, nueva_can, nuevo_pre)
                print(msg)
            else:
                print("ID no encontrado.")

        elif op == '4':
            nom = input("Ingrese nombre a buscar: ")
            resultados = inv.buscar_por_nombre(nom)
            if resultados:
                for r in resultados: print(r)
            else:
                print("No se encontraron coincidencias.")

        elif op == '5':
            productos = inv.obtener_todos()
            if productos:
                print("-" * 60)
                for p in productos: print(p)
                print("-" * 60)
            else:
                print("Inventario vacío.")

        elif op == '6':
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    mostrar_menu()
