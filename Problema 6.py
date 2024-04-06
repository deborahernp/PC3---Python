class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} ({self.año}) - ${self.precio:.2f}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al catálogo.
        """
        self.productos.append(producto)

    def mostrar_productos(self):
        """
        Muestra todos los productos en el catálogo.
        """
        for producto in self.productos:
            print(producto)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos productos
    producto1 = Producto(nombre="Bujía NGK", precio=10.95, año=2016)
    producto2 = Producto(nombre="Filtro de aceite", precio=8.50, año=2018)

    # Crear catálogo y agregar productos
    catalogo = Catalogo()
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)

    # Mostrar todos los productos en el catálogo
    print("Catálogo de productos:")
    catalogo.mostrar_productos()
