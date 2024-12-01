# Project Description
# https://dailypythonprojects.substack.com/i/145532640/how-the-project-works

"""
Build a program that has a function that takes a list of numbers and calculates their sum, 
providing the total sum as output to the user.

1. The program starts by defining a function that takes a list of numbers as input.
2. The function iterates through the list, adding each number to a running total.
3. After iterating through the list, the total sum is returned.
4. The user then prints the result using a print() function that calls the sum function and converts the output to a string.

"""

def calculate_sum(numbers):
    totalsum = sum(numbers)
    return totalsum

if __name__ == "__main__":
    # Sample list of numbers
    number_list = [1, 2, 3, 4, 5]
    result = calculate_sum(number_list)
    print(f"The total sum is: {result}")