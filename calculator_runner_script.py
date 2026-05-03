from extended_scientific_calculator import ScientificCalculator
import sys

class CalculatorConsoleInterface(ScientificCalculator):
    def __init__(self):
        self.history_log_filename = "calculation_history.txt"

    def log_calculation_to_file(self, formatted_record):
        """Saves the result to a text file with a timestamp."""
        pass
    
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
                'log', 'ln', 'exponential', 'factorial', 'abs',
                'deg_to_rad', 'rad_to_deg'
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

                if selected_operator == 'sqrt':
                    calculation_result = self.square_root(first_number)
                elif selected_operator == 'sin':
                    calculation_result = self.sin(first_number)
                elif selected_operator == 'cos':
                    calculation_result = self.cos(first_number)
                elif selected_operator == 'tan':
                    calculation_result = self.tan(first_number)
                elif selected_operator == 'asin':
                    calculation_result = self.asin(first_number)
                elif selected_operator == 'acos':
                    calculation_result = self.acos(first_number)
                elif selected_operator == 'atan':
                    calculation_result = self.atan(first_number)
                elif selected_operator == 'sinh':
                    calculation_result = self.sinh(first_number)
                elif selected_operator == 'cosh':
                    calculation_result = self.cosh(first_number)
                elif selected_operator == 'tanh':
                    calculation_result = self.tanh(first_number)
                elif selected_operator == 'asinh':
                    calculation_result = self.asinh(first_number)
                elif selected_operator == 'acosh':
                    calculation_result = self.acosh(first_number)
                elif selected_operator == 'atanh':
                    calculation_result = self.atanh(first_number)
                elif selected_operator == 'log':
                    calculation_result = self.log(first_number)
                elif selected_operator == 'ln':
                    calculation_result = self.ln(first_number)
                elif selected_operator == 'exponential':
                    calculation_result = self.exponential(first_number)
                elif selected_operator == 'factorial':
                    calculation_result = self.factorial(first_number)
                elif selected_operator == 'abs':
                    calculation_result = self.absolute_value(first_number)
                elif selected_operator == 'deg_to_rad':
                    calculation_result = self.convert_to_radians(first_number)
                elif selected_operator == 'rad_to_deg':
                    calculation_result = self.convert_to_degrees(first_number)

                final_formatted_record = f"{selected_operator}({first_number}) = {calculation_result}"

            elif selected_operator in constants:
                if selected_operator == 'pi':
                    calculation_result = self.get_pi_constant()
                elif selected_operator == 'e':
                    calculation_result = self.get_euler_constant()
                final_formatted_record = f"Constant {selected_operator} = {calculation_result}"

            else:
                raise NameError(f"The operator '{selected_operator}' is not valid.")

            print(f"RESULT: {calculation_result}")