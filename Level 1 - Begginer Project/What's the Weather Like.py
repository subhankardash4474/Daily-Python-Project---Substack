# Project Description
# https://dailypythonprojects.substack.com/i/152289844/project-description

"""
Create a program that asks the user about the current weather and, using a dictionary for decision-making, suggests an activity.

Start the script with this dictionary on top of your script:

weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}

Then, add more code so the program produces the following output.

What's the weather like today?
1. Sunny
2. Rainy
3. Cloudy
4. Snowy 
Choose 1, 2, 3, or 4: 2

Perfect weather for a cozy indoor day with a good book! 📚

Stay Safe and enjoy the weather! 🌈

1. The program prompts the user to choose 1, 2, 3, or 4 depending on the current weather.
2. Then, the program displays some text that belongs to the choice in the dictionary given further above.
"""

# Dictionary for weather activities
weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}

# Prompt the user for the current weather
choice = input("What's the weather like today? \n1. Sunny\n2. Rainy\n3. Cloudy\n4. Snowy\nChoose 1, 2, 3, or 4: ")

# Get the activity suggestion based on the user's choice
final_weather = weather_activities.get(choice)

print(final_weather)
print("Stay Safe and enjoy the weather! 🌈")