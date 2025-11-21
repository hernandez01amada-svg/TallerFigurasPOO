from figura_geometrica import FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
#se calcula area
    def area(self):
        return self.ancho * self.alto
#se calcula perimetro
    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    def __str__(self):
        return f"Rectángulo [Ancho: {self.ancho}, Alto: {self.alto}]"
if __name__ == '__main__':
    rec = Rectangulo(12, 8)
    print(rec)
    print(f"Área: {rec.area()}")
    print(f"Perímetro: {rec.perimetro()}")