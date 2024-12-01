# Project Description
# https://dailypythonprojects.substack.com/i/147959360/project-description

"""
In this project, you will create a simple program that asks the user to enter their full name, 
and the program will perform several operations to the user entry as described below.

1. First your program prompts the user to enter their name (first and last) in the terminal 
2. The user types in their name. 
3. Then, your program displays the user’s name in uppercase and then in lowercase. 
4. Next, the total number of characters is displayed. 
5. Lastly, the program reverses the user’s name and displays it.
"""

name = input("Please enter your full Name: ")
print(f"Your Name in uppercase: {(name.upper())}")
print(f"Your Name in lowercase: {(name.lower())}")
print(f"Total Number of characters (excluding space) : {len(name.replace(" ", ""))}")
print(f"Your name reversed: {name[::-1]}")