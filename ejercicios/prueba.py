import unittest
import cambia_texto

class PronarCambiaTexto(unittest.TestCase):
    def text_todo_mayusculas(self):
        self.assertEqual(cambia_texto.todo_mayusculas("hola"), "HOLA")

if __name__ == '__main__':
    unittest.main()

