import unittest
from test_calc import CalculatorUTest
from calculator import Calculator

if __name__ == '__main__':
  unittest.main(CalculatorUTest(), exit=False)

  Calculator().handle_expression('something')

  

