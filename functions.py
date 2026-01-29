'''def sum():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))  
    operation = input("Enter operation (+, -, *, /):")
    if operation == "+":
        c = a + b
        print("The sum is:", c)
    elif operation == "-":
        c = a - b
        print("The difference is:", c)
    elif operation == "*":
        c = a * b
        print("The product is:", c)
    elif operation == "/":
        c = a / b
        print("The quotient is:", c)
    else:
        c = "Invalid operation"
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print("Factorial of 5 is:", factorial(5))  # Example usage
factorial(5)

'''

def grade (marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
print("Grade for 85 is:", grade(85))  # Example usage
grade(85)



def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print("Fibonacci sequence of 10 terms:", fibonacci(10))  # Example usage