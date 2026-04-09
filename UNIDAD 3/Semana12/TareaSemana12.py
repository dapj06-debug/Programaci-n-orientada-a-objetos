# Sistema de Gestión de Biblioteca

class Libro: # Clase para representar un libro en la biblioteca
    #Método constructor para inicializar los atributos del libro
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para datos inmutables
        self.datos_base = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.datos_base[0]}' por {self.datos_base[1]} (Categoría: {self.categoria})"


class Usuario: # Clase para representar un usuario registrado en la biblioteca
    #Método constructor para inicializar los atributos del usuario
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de objetos Libro

    def __str__(self):
        return f"Usuario: {self.nombre} [ID: {self.user_id}]"

class Biblioteca: # Clase para gestionar la biblioteca, incluyendo libros y usuarios
    #Método constructor para inicializar los atributos de la biblioteca
    def __init__(self):
        # Diccionario para libros disponibles, con ISBN como clave
        self.libros_disponibles = {}  
        self.usuarios_registrados = {}  
        self.ids_usuarios = set() 

    #Método para añadir un libro a la biblioteca
    def añadir_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro añadido: {libro}")

    #Método para quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("Error: El ISBN no existe.")

    #Método para registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_usuarios:
            self.usuarios_registrados[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("Error: El ID de usuario ya existe.")

    #Método para dar de baja a un usuario
    def dar_de_baja_usuario(self, user_id):
        if user_id in self.ids_usuarios:
            usuario = self.usuarios_registrados.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"Usuario {usuario.nombre} dado de baja.")
        else:
            print("Error: Usuario no encontrado.")
  
    #Método para prestar un libro
    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros_disponibles and user_id in self.usuarios_registrados:
            libro = self.libros_disponibles.pop(isbn)
            self.usuarios_registrados[user_id].libros_prestados.append(libro)
            print(f"Libro '{libro.datos_base[0]}' prestado a {self.usuarios_registrados[user_id].nombre}.")
        else:
            print("Error: Libro o Usuario no disponible.")

    #Método para devolver un libro
    def devolver_libro(self, isbn, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            for i, libro in enumerate(usuario.libros_prestados):
                if libro.isbn == isbn:
                    libro_devuelto = usuario.libros_prestados.pop(i)
                    self.libros_disponibles[isbn] = libro_devuelto
                    print(f"Libro '{libro_devuelto.datos_base[0]}' devuelto.")
                    return
            print("Error: El usuario no tiene ese libro.")

    #Método para buscar libros
    def buscar_libro(self, criterio):
        # Búsqueda por título, autor o categoría
        resultados = [libro for libro in self.libros_disponibles.values() 
                      if criterio.lower() in libro.datos_base[0].lower() 
                      or criterio.lower() in libro.datos_base[1].lower() 
                      or criterio.lower() in libro.categoria.lower()]
        
        if resultados:
            print(f"\nResultados para '{criterio}':")
            for libro in resultados: print(f"- {libro}")
        else:
            print(f"No se encontraron libros para: {criterio}")

    #Método para listar libros prestados por un usuario
    def listar_prestados(self, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            print(f"\nLibros en préstamo para {usuario.nombre}:")
            for libro in usuario.libros_prestados: print(f"- {libro}")
        else:
            print("Error: Usuario no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Se crean algunos libros para añadir a la biblioteca
    libro1 = Libro("Fisica", "Frank Blat", "Ciencia", "1112223334445")
    libro2 = Libro("Sangre de campeón", "Carlos Cuauhtémoc Sánchez", "Literatura", "1112223334446")
    libro3 = Libro("Fabulas de Esopo", "Esopo", "Infantil", "1112223334447")

    # Se añaden los libros a la biblioteca
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Se crean algunos usuarios para registrar en la biblioteca
    usuario1 = Usuario("Diego", 1)
    usuario2 = Usuario("Armando", 2)
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Se prestan libros a los usuarios 
    biblioteca.prestar_libro("1112223334445", 1)  
    biblioteca.prestar_libro("1112223334446", 2)  

    # Se listan los libros prestados a cada usuario
    biblioteca.listar_prestados(1)  
    biblioteca.listar_prestados(2)  

    # Se devuelven los libros a la biblioteca
    biblioteca.devolver_libro("1112223334445", 1)

    # Se buscan libros por diferentes criterios
    biblioteca.buscar_libro("Frank")
    biblioteca.buscar_libro("Sangre de campeón")
    biblioteca.buscar_libro("Infantil")

    # Se da de baja a un usuario y se intenta listar sus libros prestados
    biblioteca.dar_de_baja_usuario(2)
    biblioteca.listar_prestados(2)
    
    