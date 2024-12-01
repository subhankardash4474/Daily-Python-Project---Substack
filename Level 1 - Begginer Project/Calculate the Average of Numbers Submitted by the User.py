# Project Description
# https://dailypythonprojects.substack.com/i/148688132/project-description

"""
Create a program that lets the user submit three numbers and returns the average of those numbers.

1. The program prompts the user to enter a first number in the terminal.
2. Once the user submits a number (e.g., 4), the program asks the user to submit two more numbers.
3. After submitting the third number, the program prints out a message containing the average of all three numbers. 
   The average should be in two decimal points format (e.g., 3.33).

"""

f_num = int(input("Enter the first number: "))
s_num = int(input("Enter the second number: "))
t_num = int(input("Enter the third number: "))

avg = (f_num + s_num + t_num )/3

print(f"The avergae of three numbers is: {avg:.2f} ")