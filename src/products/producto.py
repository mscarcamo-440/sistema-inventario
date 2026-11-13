class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio + 1:.2f}")
        print(f"Existencia: {self.existencia} unidades")

if __name__ == "__main__":
    Producto("P001", "Teclado", 350.00, 25).mostrar()