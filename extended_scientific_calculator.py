import math
from simple_calculator import BasicCalculator

class ScientificCalculator(BasicCalculator):
    #trigo
    def sin(self, value):
        return math.sin(math.radians(value))
    def cos(self, value):
        return math.cos(math.raians(value))
    def tan(self, value):
        return math.tan(math.radians(value))
    #inverse trigo
    def asin(self, value):
        return math.asin(math.radians(value))
    def acos(self, value):
        return math.acos(math.radians(value))
    def atan(self, value):
        return math.atan(math.radians(value))
    #hyperbolic
    def sinh(self, value):
        return math.sinh(value)
    def cosh(self, value):
        return math.cosh(value)
    def tanh(self, value):
        return math.tanh(value)
    #inverse hyperbolic
    def asinh(self, value):
        return math.asinh(value)
    def acosh(self, value):
        if value < 1:
            raise ValueError("Math Domain Error: acosh is only defined for values greater than or equal to 1.")
        return math.acosh(value)
    def atanh(self, value):
        if not (-1 < value < 1):
            raise ValueError("Math Domain Error: atanh is only defined for values between -1 and 1.")
        return math.atanh(value)