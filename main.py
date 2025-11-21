from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia

def sumar_areas(figuras):
    """Suma las áreas de figuras."""
    total_area = 0
    for figura in figuras:
        total_area += figura.area()
    return total_area

def sumar_perimetros(figuras):
    """Suma los perímetros de figuras."""
    total_perimetro = 0
    for figura in figuras:
        total_perimetro += figura.perimetro()
    return total_perimetro
def main():
    # 1. Crear dos cuadrados, dos rectángulos y una circunferencia
    c1 = Cuadrado(7)
    c2 = Cuadrado(15)
    r1 = Rectangulo(6, 7)
    r2 = Rectangulo(2, 6)
    circ1 = Circunferencia(9)

    lista_figuras = [c1, c2, r1, r2, circ1]
    print("\n Detalles de Figuras")
    for fig in lista_figuras:
        # print de objeto usando __str__, área y perímetro
        print(f"{fig} | Área: {fig.area():.2f} | Perímetro: {fig.perimetro():.2f}")

    # print de Encapsulamiento y modificación de valores
    print("\n Modificación de valores")
    print(f"Rectángulo original: {r1}")
    r1.ancho = 20  # Uso del @setter para modificar un valor
    print(f"Rectángulo modificado: {r1} | Nueva Área: {r1.area()}")
    # Cálculos Totales
    print("\n Totales Acumulados ")
    print(f"Suma total de Áreas: {sumar_areas(lista_figuras):.2f}")
    print(f"Suma total de Perímetros: {sumar_perimetros(lista_figuras):.2f}")
if __name__ == "__main__":
    main()