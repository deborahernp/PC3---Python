def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y (donde X e Y son números enteros): ")
            x, y = map(int, fraccion.split('/'))

            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            elif not (isinstance(x, int) and isinstance(y, int)):
                raise ValueError("Ambos valores deben ser números enteros.")
            elif x > y:
                raise ValueError("El numerador debe ser menor o igual al denominador.")

            return x, y
        except ValueError as ve:
            print(f"Error: {ve}. Intente nuevamente.")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}. Intente nuevamente.")

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100
    return round(porcentaje)

def main():
    x, y = obtener_fraccion()

    if x / y < 0.01:
        print("E")
    elif x / y > 0.99:
        print("F")
    else:
        print(f"{calcular_porcentaje(x, y)}%")

if __name__ == "__main__":
    main()
