# Project Description
# https://dailypythonprojects.substack.com/i/148688835/project-description
"""
Create a program that lets the user submit three numbers and the program calculates the maximum number.

1. The program prompts the user to enter a number in the terminal:
2. The user types in a number (e.g., 7) and presses Enter. The program prompts the user to enter two more numbers.
3. After the user enters the third number, the program displays a message with the maximum number 
   out of the three numbers.

"""

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if (a > b) and (a > c):
    print(f"Largest Number out of three is : {a}")
elif (b > a) and (b > c):
     print(f"Largest Number out of three is : {b}")
else:
     print(f"Largest Number out of three is : {c}")