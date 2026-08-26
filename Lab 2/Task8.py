# Task#8:
# Calculator Utility (Method Overloading Simulation):
# Create a Calculator class with method multiply() using:
# • Default arguments
# • *args
# Allow multiplication of 2, 3, or more numbers.

class Calculator:
    def multiply(self, first=1, *args):
        result = first
        for num in args:
            result *= num
        return result

calc = Calculator()

print(calc.multiply(2, 3))          
print(calc.multiply(2, 3, 4))     
print(calc.multiply(5))
