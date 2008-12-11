from AST import *
import unittest

class TestAST(unittest.TestCase):

#    def setUp(self):
#        self.seq = range(10)

    def test_evalua_nodovalor(self):
        """El evaluacion de un NodoValor ha de ser aquel con el que se ha inicializado"""
        n_valor = NodoValor(3)
        self.assertEqual(n_valor.evalua(),3)

    def test_evalua_NodoSuma(self):
      """La evaluacion de un NodoSuma ha de ser la suma de las evaluaciones de sus hijos"""
      n_suma = NodoSuma(NodoValor(2),NodoValor(3))
      self.assertEqual(n_suma.evalua(),5)

    def test_evalua_NodoProducto(self):
      """La evaluacion de un NodoProducto ha de ser el producto de las evaluaciones de sus hijos"""
      n_producto = NodoProducto(NodoValor(2),NodoValor(3))
      self.assertEqual(n_producto.evalua(),6)

    def test_evalua_combinaciones(self):
      """ """
      combinado = NodoSuma(NodoProducto(NodoValor(2),NodoValor(3)),NodoValor(4))
      self.assertEqual(combinado.evalua(),10)

    def test_presentacion_NodoValor(self):
      """La forma de presentar un NodoValor es su valor convertido a string"""
      n_valor = NodoValor(3)
      self.assertEqual(str(n_valor),"3")

    def test_presentacion_NodoSuma(self):
      """La forma de presentar un NodoSuma es la suma con el signo + de sus hijos todo entre parentesis y convertido a string"""
      n_suma = NodoSuma(NodoValor(2),NodoValor(3))
      self.assertEqual(str(n_suma),"( 2 + 3 )")

    def test_presentacion_NodoProducto(self):
      """La forma de presentar un NodoProducto es el producto con el signo * de sus hijos todo entre parentesis y convertido a string"""
      n_producto = NodoProducto(NodoValor(2),NodoValor(3))
      self.assertEqual(str(n_producto),"( 2 * 3 )")

if __name__ == '__main__':
    unittest.main()
