# Project Description
# https://dailypythonprojects.substack.com/i/150704550/project-description

"""
Your task for today is to write some code that reverses any string. There are two fundamentally different ways to accomplish this, 
one using a for-loop and another using string slicing. If you can, write both solutions.

Start your script by defining a sentence as a string. Here is an example:

text = "Python is fun!"

"The reversed string is : !nuf si nohtyP"

"""

text = "Python is fun!"
reversed_text = ''

print("Reversing the string with For Loop")
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)    

print("Reversing the string with slicing option")
print(text[::-1])