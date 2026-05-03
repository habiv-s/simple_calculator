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