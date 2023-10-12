class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b



calculator = Calculator()

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

print(f"Addition: {calculator.add(n1,n2)}")
print(f"Subtraction: {calculator.subtract(n1,n2)}")
print(f"Multiplication: {calculator.multiply(n1,n2)}")
print(f"Division: {calculator.divide(n1,n2)}")
