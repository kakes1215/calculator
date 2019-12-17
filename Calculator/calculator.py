from math import sin, cos, tan, pi


class Calculator():

    def handle_expression(self, incoming_expression):
        result = eval(incoming_expression)
        return result
