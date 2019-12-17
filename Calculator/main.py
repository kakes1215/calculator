import unittest
from tests.test_calculator import CalculatorUTest
from calculator import Calculator
from user_input import User_Input

if __name__ == '__main__':
    unittest.main(CalculatorUTest(), exit=False)
    print("******** CALCULATOR **********")
    while True:
        User_Input().get_input()
