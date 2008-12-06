class NodoSuma:
  
  def __init__(self,izdo,dcho):
    self.izdo = izdo
    self.dcho = dcho

  def evalua(self):
    return self.izdo.evalua() + self.dcho.evalua()

  def __str__(self):
    return "( " + self.izdo.__str__() + " + " + self.dcho.__str__() + " )"
    

class NodoProducto:
  
  def __init__(self,izdo,dcho):
    self.izdo = izdo
    self.dcho = dcho
    
  def evalua(self):
    return self.izdo.evalua() * self.dcho.evalua()

  def __str__(self):
    return "( " + self.izdo.__str__() + " * " + self.dcho.__str__() + " )"
    

class NodoValor:
 
  def __init__(self,valor):
    self.valor = valor
    
  def evalua(self):
    return self.valor
    
  def __str__(self):
    return str(self.valor)
