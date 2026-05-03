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

            two_number_operations = ['+', '-', '*', '/', '%', '**']
            one_number_operations = [
                'sqrt', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
                'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh',
                'log', 'ln', 'exp', 'factorial', 'abs',
                'to_rad', 'to_deg'
            ]
            constants = ['pi', 'e']

            if selected_operator in two_number_operations:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))

                if selected_operator == '+':
                    calculation_result = self.add(first_number, second_number)
                elif selected_operator == '-':
                    calculation_result = self.subtract(first_number, second_number)
                elif selected_operator == '*':
                    calculation_result = self.multiply(first_number, second_number)
                elif selected_operator == '/':
                    calculation_result = self.divide(first_number, second_number)
                elif selected_operator == '%':
                    calculation_result = self.modulus(first_number, second_number)
                elif selected_operator == '**':
                    calculation_result = self.power(first_number, second_number)

                final_formatted_record = f"{first_number} {selected_operator} {second_number} = {calculation_result}"

            elif selected_operator in one_number_operations:
                first_number = float(input("Enter value: "))