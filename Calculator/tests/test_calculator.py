import unittest
import math
from calculator import Calculator as Calc


class CalculatorUTest (unittest.TestCase):

    def test_add(self):
        self.assertEqual(2, Calc.handle_expression(self, '1 + 1'))

    def test_subtract(self):
        self.assertEqual(0, Calc.handle_expression(self, '1-1'))

    def test_multiply(self):
        self.assertEqual(1, Calc.handle_expression(self, '1*1'))

    def test_divide(self):
        self.assertEqual(1, Calc.handle_expression(self, '1/1'))

    def test_add_negative_numbers(self):
        self.assertEqual(-2, Calc.handle_expression(self, '-1+-1'))
        self.assertEqual(0, Calc.handle_expression(self, '-1+1'))
        self.assertEqual(0, Calc.handle_expression(self, '1+-1'))

    def test_subtract_negative_numbers(self):
        self.assertEqual(0, Calc.handle_expression(self, '-1--1'))
        self.assertEqual(-2, Calc.handle_expression(self, '-1-1'))
        self.assertEqual(2, Calc.handle_expression(self, '1--1'))

    def test_multiply_negative_numbers(self):
        self.assertEqual(1, Calc.handle_expression(self, '-1*-1'))
        self.assertEqual(-1, Calc.handle_expression(self, '-1*1'))
        self.assertEqual(-1, Calc.handle_expression(self, '1*-1'))

    def test_divide_negative_numbers(self):
        self.assertEqual(1, Calc.handle_expression(self, '-1/-1'))
        self.assertEqual(-1, Calc.handle_expression(self, '-1/1'))
        self.assertEqual(-1, Calc.handle_expression(self, '1/-1'))

    def test_sin(self):
        self.assertEqual(0.8414709848078965,
                         Calc.handle_expression(self, 'sin(1)'))

    def test_cos(self):
        self.assertEqual(0.5403023058681398,
                         Calc.handle_expression(self, 'cos(1)'))

    def test_tan(self):
        self.assertEqual(1.5574077246549023,
                         Calc.handle_expression(self, 'tan(1)'))

    """
    1) Parenthesis
    2) Exponents
    3) Multiplication
    4) Division
    5) Addition
    6) Subtraction
    """

    def test_pemdas(self):
        self.assertEqual(1960, Calc.handle_expression(
            self, '(4/2)-2*45+32**2*(3-1)'))
        self.assertEqual(7, Calc.handle_expression(self, '1+2*3'))
        self.assertEqual(15, Calc.handle_expression(self, '5-2+3*4'))
        self.assertEqual(8, Calc.handle_expression(self, '(2-1)+(3+4)'))
        self.assertEqual(2, Calc.handle_expression(self, '2-(1+3)+4'))
