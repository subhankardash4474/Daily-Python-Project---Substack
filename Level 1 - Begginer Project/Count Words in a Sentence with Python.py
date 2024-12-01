# Project Description
# https://dailypythonprojects.substack.com/i/151161257/project-description

"""
This project involves creating a program that takes a sentence as input and counts the number of words in that sentence.
The program will also identify the longest word in the sentence.

1. The program prompts the user to enter a sentence. 
2. Then, the program returns a message followed by the number of words in the sentence given by the user. 
3. In the last line, the program also displays the word that contains more letters in the given sentence.

"""

user_text = input("Enter a sentence: ")

new_user_text = user_text.split(" ")

print(f"Numbers of words in the sentence:  {len(new_user_text)}")

lenght_per_word = []

for word in new_user_text:
    lenght_per_word.append(len(word))

longest_word = new_user_text[lenght_per_word.index(max(lenght_per_word))]

print(f"Longest word in the sentence:  {longest_word}")