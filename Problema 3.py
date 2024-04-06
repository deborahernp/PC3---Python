class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        """
        Calcula el área del círculo utilizando la fórmula: área = π * radio^2
        """
        area = 3.14 * (self.radio ** 2)
        return area

def main():
    try:
        radio_usuario = float(input("Ingrese el radio del círculo: "))
        if radio_usuario <= 0:
            print("El radio debe ser un número positivo.")
            return

        mi_circulo = Circulo(radio_usuario)
        area_circulo = mi_circulo.calcular_area()

        print(f"El área del círculo con radio {radio_usuario} es aproximadamente {area_circulo:.2f}.")
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el radio.")

if __name__ == "__main__":
    main()
