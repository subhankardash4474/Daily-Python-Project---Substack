# Project Description
# https://dailypythonprojects.substack.com/i/149611421/project-description

"""
This program asks the user to input a number and checks whether it is positive, negative, or zero.

The program prompts the user to submit a number in the console. Once the user submits a number (e.g., -11), 
the program checks the sign of the number (e.g., negative, zero, or positive) and returns a message accordingly.

"""

number = int(input("Please enter a number: "))
if number > 0 :
    print("The number is postive")
else:
    print("The number is negative")