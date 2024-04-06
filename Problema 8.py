import random

def generar_numeros_aleatorios():
    """Genera 20 números enteros aleatorios entre 0 y 100 y devuelve una lista."""
    numeros_aleatorios = [random.randint(0, 100) for _ in range(20)]
    return numeros_aleatorios

def mostrar_lista(lista):
    """Muestra la lista obtenida por pantalla."""
    print("Lista de números aleatorios:")
    for numero in lista:
        print(numero)

def ordenar_lista(lista):
    """Ordena los valores de la lista y muestra la lista por pantalla."""
    lista.sort()
    print("Lista ordenada:")
    for numero in lista:
        print(numero)

if __name__ == '__main__':
    numeros_aleatorios = generar_numeros_aleatorios()
    mostrar_lista(numeros_aleatorios)
    ordenar_lista(numeros_aleatorios)
