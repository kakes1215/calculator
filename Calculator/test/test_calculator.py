import unittest
import math
from calculator import Calculator as Calc


class CalculatorUTest (unittest.TestCase):

    def test_add(self):
        self.assertEqual(2, Calc.handle_expression('1+1'))

    def test_subtract(self):
        self.assertEqual(0, Calc.handle_expression('1-1'))

    def test_multiply(self):
        self.assertEqual(1, Calc.handle_expression('1*1'))

    def test_divide(self):
        self.assertEqual(1, Calc.handle_expression('1/1'))
        self.assertRaises(ZeroDivisionError, Calc.handle_expression('1/0'))

    def test_add_negative_numbers(self):
        self.assertEquals(-2, Calc.handle_expression('-1+-1'))
        self.assertEquals(0, Calc.handle_expression('-1+1'))
        self.assertEquals(0, Calc.handle_expression('1+-1'))

    def test_subtract_negative_numbers(self):
        self.assertEquals(0, Calc.handle_expression('-1--1'))
        self.assertEquals(-2, Calc.handle_expression('-1-1'))
        self.assertEquals(2, Calc.handle_expression('1--1'))

    def test_multiply_negative_numbers(self):
        self.assertEquals(1, Calc.handle_expression('-1*-1'))
        self.assertEquals(-1, Calc.handle_expression('-1*1'))
        self.assertEquals(-1, Calc.handle_expression('1*-1'))

    def test_divide_negative_numbers(self):
        self.assertEquals(1, Calc.handle_expression('-1/-1'))
        self.assertEquals(-1, Calc.handle_expression('-1/1'))
        self.assertEquals(-1, Calc.handle_expression('1/-1'))

    def test_sin(self):
        self.assertEquals(0.8414709848, Calc.handle_expression('sin(1)'))
        self.assertEquals(math.pi/2, Calc.handle_expression('sin^-1(1)'))

    def test_cos(self):
        self.assertEquals(0.5403023059, Calc.handle_expression('cos(1)'))
        self.assertEquals(0, Calc.handle_expression('cos^-1(1)'))

    def test_tan(self):
        self.assertEquals(1.557407725, Calc.handle_expression('tan(1)'))
        self.assertEquals(math.pi/4, Calc.handle_expression('tan^-1(1)'))
