class Suma:
  
  def __init__(self):
    self.cat = "Suma"

  def __str__(self):
    return self.cat

class Producto:

  def __init__(self):
    self.cat = "Producto"

  def __str__(self):
    return self.cat

class Entero:

  def __init__(self,valor):
    self.cat = "Entero"
    self.valor = valor

  def __str__(self):
    return self.cat + " (valor : " + str(self.valor) + " )"

class Nl:

  def __init__(self):
    self.cat = "nl"
    
  def __str__(self):
    return self.cat


class Eof:

  def __init__(self):
    self.cat = "eof"
  
  def __str__(self):
    return self.cat
