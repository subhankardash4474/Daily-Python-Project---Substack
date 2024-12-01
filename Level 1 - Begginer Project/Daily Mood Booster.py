# Project Description 
# https://dailypythonprojects.substack.com/i/152135549/project-description
"""
Create a program that prompts the user to enter their mood (Happy, Stressed, or Tired) and 
display a message depending on the moood submitted by the user.

1. The program prompts the user to enter their name (e.g., Ardit)
2. The program greets the user with “Hi. [name]! How are you feeling today? and displays the mood options.
3. The user chooses a number (1, 2, or 3).
4. If the user is happpy, the program displays “That’s great, [name]! Keep streading your joy“
5. If the user is stressed, the program displays “Take a deep breath, [name]. You're doing amazing!“
7. If the user is tired, the program displays “Rest up, [name]. Tomorrow is a fresh start!“

"""

name = input("Hello! What your name ? ")

print(f"Hi {name} How are you felling today? \n 1. Happy \n 2. Stressed \n 3. Tired")
choice = int(input("Choose 1, 2 or 3: "))

if choice == 1:
    print(f"That’s great, {name}! Keep streading your joy")
elif choice == 2:
    print(f"Take a deep breath, {name}. You're doing amazing!")
else:
    print(f"Rest up, {name}. Tomorrow is a fresh start!")