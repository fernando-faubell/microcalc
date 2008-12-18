from lexico import *
#from componentes import *
from AST import *

class Sintactico:

  def __init__(self,lexico):
    self.lexico = lexico
    self.componente = self.lexico.siguiente()  
  
  def analizaLinea(self):
    self.analizaExpresion()
    if self.componente.cat == "eof":
      print "bien"
      
  def analizaExpresion(self):
    arbol= self.analizaTermino()
    while self.componente.cat ==  'Suma':
      self.componente= self.lexico.siguiente()
      dcho= self.analizaTermino()
      arbol= NodoSuma(arbol, dcho)
    return arbol

  
  def analizaTermino(self):
    arbol= self.analizaFactor()
    while self.componente.cat ==  'Producto':
     self.componente= self.lexico.siguiente()
     dcho= self.analizaFactor()
     arbol= NodoProducto(arbol, dcho)
    return arbol

  def analizaFactor(self):
    arbol = NodoValor(self.componente.valor)
    self.componente = self.lexico.siguiente()
    return arbol
  