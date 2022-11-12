import unittest
import math
from clases import Circulo

class ClasesTestCases(unittest.TestCase):
  def test_init(self):
    with self.assertRaises(ValueError):
      Circulo(-1)
    with self.assertRaises(ValueError):
      Circulo(0)
  
  def test_getRadio(self):
    assert(Circulo(1).getRadio() == 1)

  def test_getPerimeter(self):
    assert(Circulo(3).getPerimeter() == 2 * math.pi * 3)

  def test_getArea(self):
    assert(Circulo(3).getArea() == math.pi * 9)

  def test_setRadio(self):
    with self.assertRaises(ValueError):
      Circulo(2).setRadio(-1)
    with self.assertRaises(ValueError):
      Circulo(2).setRadio(0)

  def test_multiply(self):
    with self.assertRaises(ValueError):
      Circulo(2).multiply(-1)
    with self.assertRaises(ValueError):
      Circulo(2).multiply(0)



  