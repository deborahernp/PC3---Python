class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display_informacion(self):
        """
        Muestra toda la información del estudiante (nombre y número de registro).
        """
        print(f"Nombre del estudiante: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")

    def set_age(self, edad):
        """
        Asigna la edad al estudiante.
        """
        self.edad = edad

    def set_nota(self, nota):
        """
        Asigna una nota al estudiante.
        """
        self.notas.append(nota)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto Alumno
    mi_alumno = Alumno(nombre="Debora Hernandez", numero_registro="20170956")

    # Asignar la edad y notas
    mi_alumno.set_age(edad=26)
    mi_alumno.set_nota(nota=16)
    mi_alumno.set_nota(nota=8.5)

    # Mostrar la información del estudiante
    mi_alumno.display_informacion()
    print(f"Edad del estudiante: {mi_alumno.edad} años")
    print(f"Notas del estudiante: {mi_alumno.notas}")
