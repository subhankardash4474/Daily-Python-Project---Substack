# Project Description
# https://dailypythonprojects.substack.com/i/152183686/project-description

"""
Create a command-line app that generates secure random passwords based on user preferences. 
The user can specify the password length and whether to include uppercase letters, numbers, and special characters. 
This project focuses on randomness, string operations, and user input validation.

1. The program starts by asking the user a few questions, such as the desired password length, 
   and if there have to be any uppercase letters, numbers, or special characters in the password. 
2. Depending on the user's answers, the program generates a password and prints it out

"""
import random
import string

print("Welcome to the Password Generator!")
paswd_length = int(input("Enter the Desired password length :"))
upper = input("Include uppercase letter (yes/no) : ")
numbers = input("Include numbers (yes/no) : ")
special_character = input("Include special characters (yes/no) : ")

characters = string.ascii_lowercase  
    
if upper == 'yes':
    characters += string.ascii_uppercase
if numbers == 'yes':
    characters += string.digits
if special_character == 'yes':
    characters += string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(paswd_length))

print(f"Generated Password: {password}")