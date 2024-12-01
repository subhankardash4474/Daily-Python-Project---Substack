# Project Description
# https://dailypythonprojects.substack.com/i/148685811/project-description

"""
Create a program that checks if a number is even or odd.

1.  The program prompts the user to enter a number in the terminal.
2.  The user types in a number (e.g., 3) and presses Enter. 
3.  The program checks the number and prints out either “The number X is odd.” or “The number X is even.” 
    depending on the number.

"""

number = int(input("Enter a number:"))

if (number / 2 == 0):
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")