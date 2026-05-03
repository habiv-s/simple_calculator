from extended_scientific_calculator import ScientificCalculator
import sys

class CalculatorConsoleInterface(ScientificCalculator):
    def run_calculator(self):
        """Main interface loop that handles user inputs and manages the logic flow."""
        while True:
            print("\n" + "=" * 40)
            print("               CALCULATOR")
            print("=" * 40)

            selected_operator = input("Enter operator: ").strip().lower()