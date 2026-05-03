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