import io
import unittest
from contextlib import redirect_stdout
from src.products.producto import Producto

class TestProducto(unittest.TestCase):
    def setUp(self):
        self.producto = Producto("P001", "Teclado", 350, 10)

    def capturar_salida(self):
        salida = io.StringIO()
        with redirect_stdout(salida):
            self.producto.mostrar()
        return salida.getvalue()

    def test_cp01_crear_producto(self):
        self.assertIsInstance(self.producto, Producto)
        self.assertEqual(self.producto.codigo, "P001")
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertEqual(self.producto.precio, 350)
        self.assertEqual(self.producto.existencia, 10)

    def test_cp02_mostrar_codigo(self):
        self.assertIn("P001", self.capturar_salida())

    def test_cp03_mostrar_nombre(self):
        self.assertIn("Teclado", self.capturar_salida())

    def test_cp04_mostrar_precio(self):
        self.assertRegex(self.capturar_salida(), r"\b350(?:[.,]00)?\b")

    def test_cp05_mostrar_existencia(self):
        self.assertRegex(self.capturar_salida(), r"\b10\b")

    def test_cp06_mostrar_informacion_completa(self):
        salida = self.capturar_salida()
        self.assertIn("P001", salida)
        self.assertIn("Teclado", salida)
        self.assertRegex(salida, r"\b350(?:[.,]00)?\b")
        self.assertRegex(salida, r"\b10\b")

    def test_cp07_crear_otro_producto(self):
        segundo = Producto("P002", "Mouse", 180, 5)

        self.assertEqual(
            (segundo.codigo, segundo.nombre, segundo.precio, segundo.existencia),
            ("P002", "Mouse", 180, 5),
        )
        self.assertEqual(
            (
                self.producto.codigo,
                self.producto.nombre,
                self.producto.precio,
                self.producto.existencia,
            ),
            ("P001", "Teclado", 350, 10),
        )