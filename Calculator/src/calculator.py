from math import sin, cos, tan


class Calculator():

    def handle_expression(self, incoming_expression):
        eval(incoming_expression)
        return incoming_expression
