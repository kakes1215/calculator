import unittest
from tests.test_calculator import CalculatorUTest
from src.calculator import Calculator

if __name__ == '__main__':
    unittest.main(CalculatorUTest(), exit=False)

    print(Calculator().handle_expression('cos(1)'))
