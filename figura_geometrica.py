class FiguraGeometrica:
    def __init__(self, ancho, alto):
        # Validamos usando los setters
        self.ancho = ancho
        self.alto = alto
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError(f"El ancho debe ser mayor a 0")
        self._ancho = valor
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError(f"El alto debe ser mayor a 0.")
        self._alto = valor
    # se calcula el area
    def area(self)-> float:
        return self._ancho * self._alto
   #se calcula el perimetr"
    def perimetro(self):
        pass
    def __str__(self):
        return f"FiguraGeometrica (ancho: {self._ancho}, Alto: {self._alto})"
if __name__ == "__main__":
    figura = FiguraGeometrica(alto=15, ancho=30)
    print(figura)
    print(f"Area: {figura.area()}")