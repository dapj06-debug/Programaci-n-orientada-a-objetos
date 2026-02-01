

class CalcularAreaTriangulo: 
 
    def __init__(self, base: float, altura: float):
        #float para base y altura, para ingreso de números con decimales    
        self.base: float = base 
        self.altura: float = altura 

    #método para calcular el área del triángulo
    def calcular_area_triangulo(base: float, altura: float) -> float:
        return (base * altura) / 2

    #función para solicitar datos al usuario
    def solicitar_datos_usuario():
        # Solicitar al usuario la base y la altura del triángulo
        base_str: str = input("Introduce la base del triángulo : ") #str para ingreso de texto
        altura_str: str = input("Introduce la altura del triángulo : ") #str para ingreso de texto
        base: float = float(base_str) #float para permitir decimales
        altura: float = float(altura_str) #float para permitir decimales
        return base, altura
    
if __name__ == "__main__":
    # Solicitar datos al usuario
    base, altura = CalcularAreaTriangulo.solicitar_datos_usuario()
    
    # Crear una instancia de la clase CalcularAreaTriangulo
    triangulo = CalcularAreaTriangulo(base, altura)
    
    # Calcular el área del triángulo
    area = CalcularAreaTriangulo.calcular_area_triangulo(triangulo.base, triangulo.altura)
    
    # Mostrar el resultado al usuario
    print(f"El área del triángulo es: {area}")  

