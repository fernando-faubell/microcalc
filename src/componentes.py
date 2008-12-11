class suma:
  
  def __init__(self):
    self.cat = "Suma"

  def __str__(self):
    return self.cat

class producto:

  def __init__(self):
    self.cat = "Producto"

  def __str__(self):
    return self.cat

class entero:

  def __init__(self,valor):
    self.cat = "Entero"
    self.valor = valor

  def __str__(self):
    return self.cat + " (valor : " + str(self.valor) + " )"

class nl:

  def __init__(self):
    self.cat = "nl"
    
  def __str__(self):
    return self.cat


class eof:

  def __init__(self):
    self.cat = "eof"
  
  def __str__(self):
    return self.cat