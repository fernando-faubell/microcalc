from componentes import *

class Lexico:   

  def __init__(self,cadena):
    self.cadena = cadena
    self.pos = 0
    
  def siguiente(self):
    while True:
      if self.pos >= len(self.cadena):
        return Eof()
      elif self.cadena[self.pos] in [' ', '\t']:        
        self.pos = self.pos + 1        
      elif self.cadena[self.pos] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: 
        self.pos = self.pos + 1
        return Entero(int(self.cadena[self.pos - 1]))
      elif self.cadena[self.pos] == '+':
        self.pos = self.pos + 1 
        return Suma()
      elif self.cadena[self.pos] == '*':
        self.pos = self.pos + 1
        return Producto()
      elif self.cadena[self.pos] == '\n':
        self.pos = self.pos + 1
        return Nl()
