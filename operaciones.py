# operaciones.py

def suma(a, b):
    """
    Realiza la suma de dos números.
    """
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido"

def resta(a, b):
    """
    Realiza la resta entre dos números.
    """
    try:
        result = a - b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido"

def producto(a, b):
    """
    Realiza el producto entre dos números.
    """
    try:
        result = a * b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido"

def division(a, b):
    """
    Realiza la división entre dos números.
    """
    try:
        if b == 0:
            raise ZeroDivisionError
        result = a / b
        return result
    except (TypeError, ZeroDivisionError):
        return "Error: No es posible dividir entre cero"
