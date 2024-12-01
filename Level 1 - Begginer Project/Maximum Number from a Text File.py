# Project Description
# https://dailypythonprojects.substack.com/i/148689283/project-description

"""
In a previous project, we created a program that prompted the user to submit three numbers in the terminal and 
then the program returned the maximum number. For this project, instead of getting the numbers from the terminal, 
we will get them from a text file.

The program reads the numbers.txt file, stores the numbers in a list or similar, and returns the maximum number. 
The output should be similar to the following:

"The maximun number in the file is : 10"

"""

with open(r"C:\Users\subhanda\Downloads\VS Code Script Folder\Daily Python Project - Substack\numbers.txt", 'r') as file:
   arr =  [int(line.strip()) for line in file.readlines()]

print(f"The maximun number in the file is : {max(arr)}")