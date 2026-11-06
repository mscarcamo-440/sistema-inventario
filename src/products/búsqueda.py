from products.producto import Producto

def buscar_por_nombre(productos, texto):
    texto = texto.lower()
    return [p for p in productos if texto in p.nombre.lower()]

def buscar_por_codigo(productos, codigo):
    for p in productos:
        if p.codigo == codigo:
            return p
    return None

if __name__ == "__main__":
    inventario = [
        Producto("P001", "Teclado", 350.00, 25),
        Producto("P002", "Mouse", 180.00, 40),
        Producto("P003", "Teclado gamer", 890.00, 10),
    ]


    for p in buscar_por_nombre(inventario, "teclado"):
        p.mostrar()
        print("---")