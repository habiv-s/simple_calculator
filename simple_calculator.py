class BasicCalculator:
    def add(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number

    def divide(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("Math Error: Division by Zero")
        return first_number / second_number

    def modulus(self, first_number, second_number):
        return first_number % second_number

    def power(self, first_number, second_number):
        return first_number ** second_number

    def square_root(self, first_number):
        if first_number < 0:
            raise ValueError("Cannot calculate square root of negative number.")
        return first_number ** 0.5