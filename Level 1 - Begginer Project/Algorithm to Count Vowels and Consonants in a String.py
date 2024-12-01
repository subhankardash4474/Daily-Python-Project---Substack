# Project Description
# https://dailypythonprojects.substack.com/i/150519311/project-description

"""
This program defines a string, counts how many vowels and consonants are present, and displays both counts.

Start your script by defining a sentence as a string. Here is an example:
text = "How many vowels and consonants are in this sentence?"

The number of vowels in the string is : 15
The number of consonants in the string is : 28

"""
# Sample text
text = "How many vowels and consonants are in this sentence?"

# Initialize counts
v_counts = 0
c_counts = 0

# Define vowels
arr_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  # Including uppercase vowels

# Remove spaces from the text for accurate counting
new_text = text.replace(" ", "")

# Count vowels and consonants
for char in new_text:
    if char.isalpha():  # Check if the character is a letter
        if char in arr_vowels:
            v_counts += 1  # Increment vowel count
        else:
            c_counts += 1  # Increment consonant count

print(f"The number of vowels in the string is : {v_counts}")
print(f"The number of consonants in the string is : {c_counts}")