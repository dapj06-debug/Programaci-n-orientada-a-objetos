
def calcular_area_triangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo dado su base y altura."""
    return (base * altura) / 2

def solicitar_datos_usuario() -> tuple:
    """Solicita al usuario la base y altura del triángulo."""
    base_str: str = input("Introduce la base del triángulo (en unidades): ")
    altura_str: str = input("Introduce la altura del triángulo (en unidades): ")
    base: float = float(base_str)
    altura: float = float(altura_str)
    return base, altura

def main():
    continuar: bool = True
    while continuar:
        base_triangulo, altura_triangulo = solicitar_datos_usuario()
        area_triangulo: float = calcular_area_triangulo(base_triangulo, altura_triangulo)
        print(f"El área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_triangulo}")
        

if __name__ == "__main__":
    main()
