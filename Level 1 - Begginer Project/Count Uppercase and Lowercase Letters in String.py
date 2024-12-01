# Project Description
# https://dailypythonprojects.substack.com/i/150520433/project-description

"""
This program defines a string, counts how many uppercase and lowercase letters are present, and displays both counts.

Start your script by defining a sentence as a string. Here is an example:

text = "This Sentence Has Mixed CASE Letters!"

Here is how the program behaves when run:

The number of uppercase in the string is : 9
The number of lowercase in the string is : 22

"""

# Sample text
text = "This Sentence Has Mixed CASE Letters!"

# Initialize counts
u_counts = 0
l_counts = 0

# Remove spaces from the text for accurate counting
new_text = text.replace(" ", "")

# Count uppercase and lowercase
for char in new_text:
    if char.isalpha():  # Check if the character is a letter
        if char.isupper():
            u_counts += 1 
        elif char.islower():
            l_counts += 1  

print(f"The number of uppercase in the string is : {u_counts}")
print(f"The number of lowercase in the string is : {l_counts}")