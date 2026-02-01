
# Definición de clase para representar al personal de una empresa
class persona:
    #encapsulamiento de atributos
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    #abstraccion de metodo

    def mostrar_datos(self): #muestra los datos de la persona
            
        print("Nombre:", self.nombre)
        print("Cédula:", self.cedula)
        print("Dirección:", self.direccion)
        print("Teléfono:", self.telefono)
        print("Correo:", self.correo)

    #herencia y polimorfismo
class empleado(persona): #clase empleado que hereda de persona
    
    def __init__(self, nombre, cedula, direccion, telefono, correo, sueldo, puesto): 
        super().__init__(nombre, cedula, direccion, telefono, correo)
        #atributos adicionales para empleado
        self.sueldo = sueldo 
        self.puesto = puesto

    def mostrar_datos(self): 
        super().mostrar_datos() #llama al metodo mostrar_datos de la clase padre
         #muestra los datos adicionales del empleado
        print("Sueldoo:", self.sueldo)
        print("Puesto:", self.puesto)


#clase para pagos
class pago: 
    #atributos de la clase pago
    def __init__(self, empleado, monto, fecha):
        self.empleado = empleado
        self.monto = monto
        self.fecha = fecha

    #abstraccion de metodo
    def mostrar_pago(self):
        print("Pago realizado a:", self.empleado.nombre)
        print("Monto:", self.monto)
        print("Fecha:", self.fecha)

#ejemplo de uso de las clases
if __name__ == "__main__":
    empleado1 = empleado("Juan ", "1234567890", "Calle ", "0987654321", "ejemplo@gmail.com", 800.00, "Desarrollador")
    empleado1.mostrar_datos()
    pago1 = pago(empleado1, 800.00, "2025-10-01")
    pago1.mostrar_pago()



    