# Project Description
# https://dailypythonprojects.substack.com/i/150304486/project-description

"""
This program creates a function that checks whether a username is valid based on some simple rules. 
The function will take a username as input and return whether it is valid or not. 

The rules for a valid username are:
1. The username must be between 5 and 15 characters.
2. It must contain only alphanumeric characters (letters and numbers).
3. It must start with a letter.

"""


def check_username_validity(username):
    # Check if the length of the username is between 5 and 15 characters
    if len(username) < 5 or len(username) > 15:
        return "Invalid username: Length must be between 5 and 15 characters."

    # Check if the username contains only alphanumeric characters
    if not username.isalnum():
        return "Invalid username: Must contain only alphanumeric characters."

    # Check if the first character of the username is a letter
    if not username[0].isalpha():
        return "Invalid username: Must start with a letter."

    # If all conditions are met
    return "Valid username."

username = input("Enter a username: ")
print(check_username_validity(username))