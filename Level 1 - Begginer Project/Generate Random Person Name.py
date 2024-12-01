# Project Description
# https://dailypythonprojects.substack.com/i/151545141/project-description

"""
Create a program that reads a list of names from a text file, randomly picks one, and displays it. 
It's perfect for practicing file handling and working with lists in Python.

"""

import random

with open(r"C:\Users\subhanda\Downloads\VS Code Script Folder\Daily Python Project - Substack\names.txt", 'r') as file:
    names = [str(line.strip()) for line in file.readlines()]

print(f"Ramdon Name from the txt file: {random.choice(names)}")