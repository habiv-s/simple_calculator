from extended_scientific_calculator import ScientificCalculator
import sys

class CalculatorConsoleInterface(ScientificCalculator):
    def run_calculator(self):
        """Main interface loop that handles user inputs and manages the logic flow."""
        while True:
            print("\n" + "=" * 40)
            print("               CALCULATOR")
            print("=" * 40)

            print("""               OPERATORS

            two_number_operations: + - * / % **

            one_number_operations:
            sqrt sin cos tan asin acos atan
            sinh cosh tanh asinh acosh atanh
            log ln exponential factorial
            abs deg_to_rad rad_to_deg

            constants: pi e""")
            print("=" * 40)

            selected_operator = input("Enter operator: ").strip().lower()