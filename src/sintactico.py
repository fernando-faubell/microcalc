class Sintactico:

  def __init__(self,lexico):
    self.lexico = lexico
    #self.componente = self.lexico.siguiente()
  
  
  
  def analizaLinea(self):
    pass
  
  def analizaExpresion(self):
   arbol= self.analizaTermino()
   while self.componente.cat ==  'suma':
     self.componente= self.lexico.siguiente()
     dcho= self.analizaTermino()
     arbol= AST.NodoSuma(arbol, dcho)
   return arbol

  
  def analizaTermino(self):
    pass
  
  def analizaFactor(self):
    pass
  