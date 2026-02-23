# Gestion de Inventarios - Semana 10

# importamos el módulo os para manejar archivos y directorios
import os

# clase producto
class Producto:

    # constructor de la clase producto
    def __init__(self, ID, nombre, cantidad, precio):
        self._ID = ID
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # getters y setters para cada atributo
    def get_ID(self):
        return self._ID

    def set_ID(self, ID):
        self._ID = ID

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    # método para representar el producto como una cadena legible
    def __str__(self):
        return f"ID: {self._ID}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"

# clase inventario para gestionar los productos
class Inventario:
    # constructor de la clase inventario
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # método para cargar productos desde un archivo de texto
    def cargar_desde_archivo(self):
        # si el archivo no existe, se crea uno nuevo
        if not os.path.exists(self.archivo):
            # try-except para manejar posibles errores al crear el archivo
            try:
                # with para que el archivo se cierre después de su uso
                with open(self.archivo, 'w', encoding='utf-8') as f:
                    pass
            # except para manejar el error de permisos al intentar crear el archivo
            except PermissionError:
                print(f"Error: No se tienen permisos para crear el archivo {self.archivo}.")
                return

        # try-except para manejar posibles errores al leer el archivo
        try:
            # with para que el archivo se cierre después de su uso
            with open(self.archivo, 'r', encoding='utf-8') as f:
                self.productos = []
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        partes = linea.split('|')
                        if len(partes) == 4:
                            ID, nombre, cantidad, precio = partes
                            try:
                                cantidad = int(cantidad)
                                precio = float(precio)
                                prod = Producto(ID, nombre, cantidad, precio)
                                self.productos.append(prod)
                            except ValueError:
                                continue
        # except para manejar el error de archivo no encontrado al intentar leer el archivo
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print(f"Error: No se tienen permisos para leer el archivo {self.archivo}.")

    # método para guardar los productos en el archivo de texto
    def guardar_en_archivo(self):
        # try-except para manejar posibles errores al escribir en el archivo
        try:
            # with para que el archivo se cierre después de su uso
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for p in self.productos:
                    f.write(f"{p.get_ID()}|{p.get_nombre()}|{p.get_cantidad()}|{p.get_precio()}\n")
            return True
        # except para gestionar el error de archivo no encontrado al intentar escribir en el archivo
        except PermissionError:
            print(f"Error: No se tienen permisos para escribir en el archivo {self.archivo}.")
            return False

    # método para añadir un nuevo producto al inventario, verificando que el ID sea único
    def añadir_producto(self, producto):
        if any(p.get_ID() == producto.get_ID() for p in self.productos):
            return False, "El ID ya existe."
        self.productos.append(producto)
        if self.guardar_en_archivo():
            return True, "Producto añadido exitosamente."
        else:
            self.productos.pop()
            return False, "Error al guardar el producto en archivo."

    # método para eliminar un producto del inventario por su ID, verificando que el producto exista
    def eliminar_producto(self, ID):
        for i, p in enumerate(self.productos):
            if p.get_ID() == ID:
                del self.productos[i]
                if self.guardar_en_archivo():
                    return True, "Producto eliminado exitosamente."
                else:
                    self.productos.insert(i, p)
                    return False, "Error al guardar cambios en archivo."
        return False, "Producto no encontrado."

    # metodo para modificar la cantidad o el precio
    def actualizar_producto(self, ID, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_ID() == ID:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                if self.guardar_en_archivo():
                    return True, "Producto actualizado exitosamente."
                else:
                    return False, "Error al guardar cambios en archivo."
        return False, "Producto no encontrado."

    # método para buscar productos
    def buscar_por_nombre(self, nombre):
        nombre = nombre.lower()
        return [p for p in self.productos if nombre in p.get_nombre().lower()]

    # método para mostrar todos los productos en el inventario
    def mostrar_todos(self):
        return self.productos

# interfaz de la consola
def menu():
    # instancia de la clase inventario para gestionar los productos
    inventario = Inventario()
    # bucle para mostrar el menú y procesar las opciones seleccionadas por el usuario
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            ID = input("Ingrese ID único del producto: ").strip()
            nombre = input("Ingrese nombre del producto: ").strip()
            # try-except para manejar posibles errores
            try:
                cantidad = int(input("Ingrese cantidad: ").strip())
                precio = float(input("Ingrese precio: ").strip())
            except ValueError:
                print("Cantidad debe ser entero y precio debe ser número decimal.")
                continue
            prod = Producto(ID, nombre, cantidad, precio)
            exito, mensaje = inventario.añadir_producto(prod)
            print(mensaje)
        elif opcion == '2':
            ID = input("Ingrese ID del producto a eliminar: ").strip()
            exito, mensaje = inventario.eliminar_producto(ID)
            print(mensaje)
        elif opcion == '3':
            ID = input("Ingrese ID del producto a actualizar: ").strip()
            cantidad = None
            precio = None
            cambiar_cantidad = input("¿Desea actualizar la cantidad? (s/n): ").strip().lower()
            if cambiar_cantidad == 's':
                # try-except para manejar posibles errores al ingresar la cantidad
                try:
                    cantidad = int(input("Ingrese nueva cantidad: ").strip())
                except ValueError:
                    print("Cantidad debe ser un número entero.")
                    continue
            cambiar_precio = input("¿Desea actualizar el precio? (s/n): ").strip().lower()
            if cambiar_precio == 's':
                # try-except para manejar posibles errores al ingresar el precio
                try:
                    precio = float(input("Ingrese nuevo precio: ").strip())
                except ValueError:
                    print("Precio debe ser un número decimal.")
                    continue
            if cantidad is None and precio is None:
                print("No se realizó ninguna actualización.")
                continue
            exito, mensaje = inventario.actualizar_producto(ID, cantidad, precio)
            print(mensaje)
        elif opcion == '4':
            nombre = input("Ingrese nombre o parte del nombre a buscar: ").strip()
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                print(f"Se encontraron {len(resultados)} producto(s):")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == '5':
            productos = inventario.mostrar_todos()
            if productos:
                print("Productos en inventario:")
                for p in productos:
                    print(p)
            else:
                print("El inventario está vacío.")
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
