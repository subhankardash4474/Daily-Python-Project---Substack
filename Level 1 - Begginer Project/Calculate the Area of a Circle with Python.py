# Project Description
# https://dailypythonprojects.substack.com/i/149610518/project-description

"""
Your task for today is to create a Python program that calculates the area of a circle.

1. The program starts by prompting the user to submit the radius of the circle. Once the user submits a number (e.g., 22), 
the program displays a message that includes the area of the circle.
2. Note that the area is shown with two decimal points.

"""

radius = float(input("Enter the radius of the circle: "))

print(f"Area of the circle is : {(3.14 * radius * radius):.2f}")