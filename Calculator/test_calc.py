import unittest
from calculator import Calculator as Calc

class CalculatorUTest (unittest.TestCase):

  def test_add(self):
    self.assertEqual(2, Calc.handle_expression('1+1'))
    self.assertEqual(2, Calc.handle_expression('1+1'))
    self.assertEqual(2, Calc.handle_expression('1+1'))


