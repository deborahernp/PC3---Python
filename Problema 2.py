def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones = entrada.split(',')
            calificaciones_enteras = [int(cal) for cal in calificaciones]
            return calificaciones_enteras
        except ValueError:
            print("¡Error! Asegúrate de ingresar números enteros separados por comas. Inténtalo nuevamente.")

def main():
    calificaciones_enteras = obtener_calificaciones()
    print("Calificaciones enteras:", calificaciones_enteras)

if __name__ == "__main__":
    main()
