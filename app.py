# app.py

def greet(name):
    print(f"Hello, {name}! Welcome to Python learning.")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")
