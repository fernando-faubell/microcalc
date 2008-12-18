from lexico import *
import unittest

class TestLexico(unittest.TestCase):

  def test_atributos(self):
    """Un Objeto Lexico ha de tener pos = 0 y cadena la cadena pasada"""
    o_Lexico = Lexico("3+2")
    self.assertEqual(o_Lexico.pos,0)
    self.assertEqual(o_Lexico.cadena,"3+2")

  def test_siguiente_con_suma(self):
    """ """
    o_Lexico = Lexico(" 2 + 3 ")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Entero), "Siguiente no es un entero")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Suma), "Siguiente no es una suma")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Entero), "Siguiente no es un entero")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Eof), "Siguiente no es un final de fichero")

  def test_siguiente_con_producto(self):
    """ """
    o_Lexico = Lexico(" 2 * 3 ")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Entero), "Siguiente no es un entero")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Producto), "Siguiente no es un producto")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Entero), "Siguiente no es un entero")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Eof), "Siguiente no es un final de fichero")

  def test_siguiente_con_suma_y_nl(self):
    """ """
    o_Lexico = Lexico(" 2 + 3 \n")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Entero), "Siguiente no es un entero")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Suma), "Siguiente no es una suma")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Entero), "Siguiente no es un entero")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Nl), "Siguiente no es final de linea")
    self.assertTrue(isinstance(o_Lexico.siguiente(),Eof), "Siguiente no es un final de fichero")


if __name__ == '__main__':
  unittest.main()
