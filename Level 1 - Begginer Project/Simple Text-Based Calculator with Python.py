# Project Description
# https://dailypythonprojects.substack.com/i/149914612/project-description

"""
Build a program that the user to input two numbers and an operation (addition, subtraction, multiplication, or division). 
It performs the operation on the two numbers and displays the result.

1. The program lets the user input two numbers (e.g., 4 and 8). 
2. Then, the program lets the user input an operation (e.g., * for multiplication). 
3. Finally, the program displays the result of the operation.

"""

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

operation = input("Enter the mathametical opertaion(+ , - , * , / ): ")

if operation == '+':
    cal = number_1 + number_2
elif operation == '-':
    cal = number_1 - number_2
elif operation == '*':
    cal = number_1 * number_2
else:
    cal = number_1 / number_2

print(f"The result of the operation is : {cal:.2f}")