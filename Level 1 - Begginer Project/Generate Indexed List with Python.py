# Project Description
# https://dailypythonprojects.substack.com/i/146757098/project-description

"""
This project involves creating a program that takes a list of elements, processes it using list comprehension,
and returns a new list that pairs each element with its index in the original list.

1. Add this line on top of an empty Python script:
        mylist = ['a', 'b', 'c']
2. In the script, iterate over that list using a for-loop or preferably a list comprehension to produce the following list of tuples:
        [('a', 0), ('b', 1), ('c', 2)]
3. Each tuple in this new list consists of an element from the original list paired with its corresponding index.
4. The output of the program should be the text “Indexed list:” followed by the newly produced list.

"""
mylist = ['a', 'b', 'c']

indexed_list = []

for value in mylist:
    indexed_list.append((value, mylist.index(value)))

print(f"Indexed list: {indexed_list}")