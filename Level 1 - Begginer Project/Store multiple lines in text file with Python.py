# Project Description
# https://dailypythonprojects.substack.com/i/148443066/how-the-project-works

"""
This project is designed for beginner learners who are still learning and practicing Python fundamentals.

1.  Your program should ask the user to enter three sentences:
2.  Once the user has submitted the sentences, the program prints out a message saying that the sentences 
    have been saved in a text file.
3.  The sentences are stored in a text file and there should be dash lines between the sentences.
    Here is what the text file should look like:

"""
value = []

for i in range(3):
    sentence = input(f"Enter Sentence {i+1} :")
    value.append(sentence)
    value.append("----------")

with open("user_sentences.txt",'w') as file:
    file.write('\n'.join(value))
print("Sentences have been stored to user_sentences.txt file")