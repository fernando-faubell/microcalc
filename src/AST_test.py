from AST import *
import unittest

class TestAST(unittest.TestCase):

#    def setUp(self):
#        self.seq = range(10)

    def test_evalua_nodovalor(self):
        # La evaluacion de NodoValor ha de ser el valor almacenado
        n_valor = NodoValor(3)
        self.assertEqual(n_valor.evalua(),3)

    def test_evalua_NodoSuma(self):
      n_suma = NodoSuma(NodoValor(2),NodoValor(3))
      self.assertEqual(n_suma.evalua(),5)

    def test_evalua_NodoProducto(self):
      n_producto = NodoProducto(NodoValor(2),NodoValor(3))
      self.assertEqual(n_producto.evalua(),6)

    def test_evalua_combinaciones(self):
      combinado = NodoSuma(NodoProducto(NodoValor(2),NodoValor(3)),NodoValor(4))
      self.assertEqual(combinado.evalua(),10)

    def test_presentacion_NodoValor(self):
      n_valor = NodoValor(3)
      self.assertEqual(str(n_valor),"3")

    def test_presentacion_NodoSuma(self):
      n_suma = NodoSuma(NodoValor(2),NodoValor(3))
      self.assertEqual(str(n_suma),"( 2 + 3 )")

    def test_presentacion_NodoProducto(self):
      n_producto = NodoProducto(NodoValor(2),NodoValor(3))
      self.assertEqual(str(n_producto),"( 2 * 3 )")



        

if __name__ == '__main__':
    unittest.main()
