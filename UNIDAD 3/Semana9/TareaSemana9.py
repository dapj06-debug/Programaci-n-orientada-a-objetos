
class Producto:
    #método constructor de la clase producto
    def __init__ (self, id_producto, nombre, cantidad, precio):
        #atributos de la clase producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    #método para mostrar la información del producto
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
    
class Inventario:
        def __init__(self): 
            self.productos = []
        #método para agregar un producto al inventario, id unico para cada producto
        def agregar_producto(self, producto):
            for p in self.productos:
                if p.id_producto == producto.id_producto:
                    print("Error: El ID del producto ya existe en el inventario.")
                    return
            self.productos.append(producto)
            print("Producto agregado al inventario.")
        #método para eliminar un producto del inventario por su id
        def eliminar_producto(self, id_producto):
            for p in self.productos:
                if p.id_producto == id_producto:
                    self.productos.remove(p)
                    print("Producto eliminado del inventario.")
                    return
            print("Error: Producto no encontrado en el inventario.")
        #metodo para modificcar precio o cantidad de un producto por su id
        def modificar_producto(self, id_producto, nuevo_precio=None, nueva_cantidad=None):
            for p in self.productos:
                if p.id_producto == id_producto:
                    if nuevo_precio is not None:
                        p.precio = nuevo_precio
                    if nueva_cantidad is not None:
                        p.cantidad = nueva_cantidad
                    print("Producto modificado en el inventario.")
                    return
            print("Error: Producto no encontrado en el inventario.")
        #método para buscar productos por nombre
        def buscar_producto(self, nombre):
            resultados = []
            for p in self.productos:
                if p.nombre.lower() == nombre.lower():
                    resultados.append(p)
            return resultados
        #método para mostrar todos los productos en el inventario
        def mostrar_inventario(self):
            if not self.productos:
                print("El inventario está vacío.")
            else:
                for p in self.productos:
                    print(p)
                    
#interfaz de consola para el usuario
    
def main():
    inventario = Inventario()
    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Modificar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        
        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        
        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a modificar: ")
            nuevo_precio = input("Ingrese el nuevo precio (deje en blanco para no modificar): ")
            nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco para no modificar): ")
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            inventario.modificar_producto(id_producto, nuevo_precio, nueva_cantidad)
        
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")
        
        elif opcion == "5":
            inventario.mostrar_inventario()
        
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
if __name__ == "__main__":
    main()