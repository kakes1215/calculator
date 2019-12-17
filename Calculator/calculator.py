from math import sin, cos, tan, pi, e, factorial, sqrt, sinh, cosh, tanh, gcd, hypot, inf, log, log10, log1p, log2, radians, degrees, remainder


class Calculator():

    def handle_expression(self, incoming_expression):
        result = eval(incoming_expression)
        return result
