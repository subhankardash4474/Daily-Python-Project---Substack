# Project Description
# https://dailypythonprojects.substack.com/i/148187916/project-description

"""
This program asks the user to enter their birth year and the current year. 
It then calculates and displays the user's age.

1. The program starts by asking the user to enter their birth year.
2. Next, it asks the user to enter the current year.
3. The program calculates the user's age by subtracting the birth year from the current year.
4. Finally, it displays a message in the terminal that includes the calculated age.

"""

b_year = int(input("Enter your birth Year: "))
c_year = int(input("Enter current Year:"))
age = c_year - b_year
print(f"You are {age} old.")