#Programación tradicional

def area_rectangulo(base, altura): #Calculo del área de un rectángulo
    return base * altura 

def area_circulo(radio):#Calculo del área de un círculo
    import math #Importar la biblioteca matemática para usar pi
    return math.pi * (radio ** 2)

#Ejemplos

#Definicion de variables para el rectángulo y el círculo
rectangulo = {
    'base': 10,
    'altura': 5
} 

circulo = {
    'radio': 7
}

#Cálculo de áreas usando las funciones definidas

print("El área del rectángulo es:", area_rectangulo(rectangulo['base'], rectangulo['altura']))
print("El área del círculo es:", area_circulo(circulo['radio']))




#Programación orientada a objetos

#Definición de la clase base Figura_geometrica
class Figura_geometrica:
    #Metodo para calcular 
    def perimetro(self):
        pass
    def area(self):
        pass
    def volumen(self):
        pass

#Definición de la clase Rectangulo que hereda de Figura_geometrica
class Rectangulo(Figura_geometrica):
    #Encapsulamiento de atributos 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    #Metodo para calcular el área del rectángulo
    def area(self):
        return self.base * self.altura

#Creación de una instancia de Rectangulo y cálculo del área     
rectangulo_1 = Rectangulo(20, 10)
print("El área del rectángulo:", rectangulo_1.area())

#Definición de la clase Circulo que hereda de Figura_geometrica
class Circulo(Figura_geometrica):
    #Encapsulamiento del atributo 
    def __init__(self, radio):
        self.radio = radio

    #Metodo para calcular el área del círculo
    def area(self):
        import math
        return math.pi * (self.radio ** 2)
    
#Creación de una instancia de Circulo y cálculo del área    
circulo_1 = Circulo(5)
print("El área del círculo:", circulo_1.area())




    


  
