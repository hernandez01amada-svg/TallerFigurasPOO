import math
from figura_geometrica import FiguraGeometrica
class Circunferencia(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__(radio, radio)
    def area(self):
        return math.pi * (self.ancho ** 2)
    def perimetro(self):
        return 2 * math.pi * self.ancho
    def __str__(self):
        return f"Circunferencia [Radio: {self.ancho}]"
if __name__ == '__main__':
    cir = Circunferencia(3)
    print(cir)
    print(f"Área: {cir.area():.2f}")
    print(f"Perímetro: {cir.perimetro():.2f}")