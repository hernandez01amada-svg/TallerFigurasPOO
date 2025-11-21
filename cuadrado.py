from figura_geometrica import FiguraGeometrica
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        # Utilizamos 'lado' para ancho y alto
        super().__init__(lado, lado)
        #se calcula area
    def area(self):
        return self.ancho * self.alto
#se calcula perimetro
    def perimetro(self):
        return 4 * self.ancho
    def __str__(self):
        return f"Cuadrado [Lado: {self.ancho}]"
if __name__ == '__main__':
    c = Cuadrado(7)
    print(c)
    print(f"Área: {c.area()}")
    print(f"Perímetro: {c.perimetro()}")
