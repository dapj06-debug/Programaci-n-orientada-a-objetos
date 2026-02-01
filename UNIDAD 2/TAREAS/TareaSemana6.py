class Usuario:
    def __init__(self, nombre, cedula):
        #encapsulamiento de atributos
        self.__nombre = nombre
        self.__cedula = cedula
        self.asistencias = 0

    #metodo para obtener el nombre
    def get_nombre(self):
        return self.__nombre
    
    #metodo para obtener la cedula
    def get_cedula(self):
        return self.__cedula
    
    #metodo para registrar asistencia
    def registrar_asistencia(self):
        self.asistencias += 1
        print(f"Asistencia registrada para {self.__nombre}. Total asistencias: {self.asistencias}")


class Estudiante(Usuario):

    #constructor de la clase Estudiante
    def __init__(self, nombre, cedula, carrera):
        #llamada al constructor de la clase Usuario
        super().__init__(nombre, cedula)
        self.carrera = carrera

    #metodo sobreescrito para registrar asistencia
    def registrar_asistencia(self):
        self.asistencias += 1
        print(f"Asistencia registrada para el estudiante {self.get_nombre()} de la carrera {self.carrera}. Total asistencias: {self.asistencias}")

    
class Profesor(Usuario):

    #constructor de la clase Profesor
    def __init__(self, nombre, cedula, materia):
        #llamada al constructor de la clase Usuario
        super().__init__(nombre, cedula)
        self.materia = materia 
    #metodo sobreescrito para registrar asistencia
    def registrar_asistencia(self):
        self.asistencias += 1
        print(f"Asistencia registrada para el profesor {self.get_nombre()} de la materia {self.materia}. Total asistencias: {self.asistencias}")

#ejecucion del programa
def menu():
    registros = []
    while True:
        print("REGISTRO DE ASISTENCIAS")
        print("1. Registrar Estudiante")
        print("2. Registrar Profesor")
        print("3. Marcar Asistencia")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            cedula = input("Ingrese la cédula del estudiante: ")
            carrera = input("Ingrese la carrera del estudiante: ")
            estudiante = Estudiante(nombre, cedula, carrera)
            registros.append(estudiante)
            print("Estudiante registrado exitosamente.\n")
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del profesor: ")
            cedula = input("Ingrese la cédula del profesor: ")
            materia = input("Ingrese la materia del profesor: ")
            profesor = Profesor(nombre, cedula, materia)
            registros.append(profesor)
            print("Profesor registrado exitosamente.\n")
        
        elif opcion == '3':
            cedula = input("Ingrese la cédula del usuario: ")
            encontrado = False
            for usuario in registros:
                if usuario.get_cedula() == cedula:
                    usuario.registrar_asistencia()
                    encontrado = True
                    break
            if not encontrado:
                print("Usuario no encontrado.\n")  
            
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.\n")
if __name__ == "__main__":
    menu()  
