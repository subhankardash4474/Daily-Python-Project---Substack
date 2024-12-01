# Project Description
# https://dailypythonprojects.substack.com/i/150836277/how-the-project-works

"""
This project simulates a dice roll by generating a random number between 1 and 6. Each time the program runs,
it "rolls the dice" and displays the result. This project introduces students to working with random numbers 
and basic output formatting.

The program will use Python’s random module to simulate rolling a six-sided die. Any time the program runs, 
it displays am message containing the random number
"""

import random

dice_arr = ['1', '2', '3', '4', '5', '6']
dice_value = random.choice(dice_arr)
print(f"You rolled a {dice_value}! ")