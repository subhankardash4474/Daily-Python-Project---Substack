# Python Description
# https://dailypythonprojects.substack.com/i/149300879/project-description

"""
Your task for today is to create a Python program which generates a new text file every time you run it.

When you run the program, it should generate a new text file. 
The program assigns a random name of 10 characters to the text file and also writes that random 
text inside the text file as content.
Any time the program is executed, a new file with a different name is generted.

"""

import random
import string

random_string = ''.join(random.choices(string.ascii_letters, k=10))
random_file = ''.join(random.choices(string.ascii_letters, k=10))

with open(f'C:\\Users\\subhanda\\Downloads\\VS Code Script Folder\\Daily Python Project - Substack\\{random_file}.txt', 'w') as file:
    file.write(random_string)