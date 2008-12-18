from componentes import *
import unittest

class TestComponentes(unittest.TestCase):


  def test_categoria_Suma(self):
    """Un Objeto Suma ha de tener cat = Suma"""
    o_Suma = Suma()
    self.assertEqual(o_Suma.cat,'Suma')

  def test_categoria_Producto(self):
    """Un Objeto Producto ha de tener cat = Producto"""
    o_Producto = Producto()
    self.assertEqual(o_Producto.cat,'Producto')

  def test_categoria_Entero(self):
    """Un Objeto Entero ha de tener cat = Entero y valor la cantidad con la que se inicializa"""
    o_Entero = Entero(3)
    self.assertEqual(o_Entero.cat,'Entero')
    self.assertEqual(o_Entero.valor,3)

  def test_categoria_Nl(self):
    """Un Objeto Nl ha de tener cat = Nl"""
    o_Nl = Nl()
    self.assertEqual(o_Nl.cat,'nl')

  def test_categoria_Eof(self):
    """Un Objeto Eof ha de tener cat = eof"""
    o_Eof = Eof()
    self.assertEqual(o_Eof.cat,'eof')

#  def test_representacion_Suma(self):
#    """ """
#    o_Suma = Suma()    
#    self.asserEqual(o_Suma.__str__(),'Suma')


if __name__ == '__main__':
  unittest.main()
