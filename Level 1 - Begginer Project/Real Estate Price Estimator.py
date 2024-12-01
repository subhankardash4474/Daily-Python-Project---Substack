# Project Description
# https://dailypythonprojects.substack.com/i/151819212/project-description

"""
This is a simple beginner project where the program estimates the price of a property based on the size of the house 
(in square feet) and its location (city or suburb). The program will help practice basic Python concepts 
such as user input, conditional statements, and basic calculations.

1. The program starts by prompting the user to enter the square feet of the property.
2. Next, the program asks to enter “city” or “suburb”. If the user submits “city”, the program should use a price of 250 dollars per square foot. 
   If they submit “suburb”, the program should use a price of 150 dollars per square foot.
3. After the user has submitted “city” or “suburb”, the program displays a message where it includes the estimated price for the given property.

"""

print("Welcome to the Real Estate Price Calculator")
sqft = float(input("Enter the size of the property in square feet: "))
loaction = input("Enter the location(city ot suburb): ")

if loaction.lower() == "city":
    sqftprice = 250
else:
    sqftprice = 150

final_price = sqft * sqftprice

print(f"The estimated price for {sqft} property in the {loaction.lower()} : {final_price}$ .")