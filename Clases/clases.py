import math

class Circulo():
  def __init__(self, radio):
    if radio <= 0:
      raise ValueError('El radio debe ser mayor a cero')
    self.__radio = radio

  def getRadio(self):
    return self.__radio

  def setRadio(self, radio):
    if radio <= 0:
      raise ValueError('El radio debe ser mayor que cero')
    self.__radio = radio

  def getPerimeter(self):
    return 2 * math.pi * self.__radio

  def getArea(self):
    return math.pi * (self.__radio ** 2)

  def multiply(self, n):
    if n <= 0:
      raise ValueError('El número a multiplicar debe ser mayor que cero')
    return Circulo(self.__radio * n)

  def __str__(self):
    txt = 'Circunferencia de radio {0}, perímetro {1} y área {2}.'
    return txt.format(str(self.__radio), str(round(self.getPerimeter(),2)), str(round(self.getArea(),2)))