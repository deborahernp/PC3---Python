class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        """
        Calcula el área del rectángulo multiplicando el largo por el ancho.
        """
        return self.largo * self.ancho

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un rectángulo con largo 5 y ancho 3
    mi_rectangulo = Rectangulo(largo=5, ancho=3)
    area_rectangulo = mi_rectangulo.calcular_area()
    print(f"El área del rectángulo es: {area_rectangulo} unidades cuadradas")
