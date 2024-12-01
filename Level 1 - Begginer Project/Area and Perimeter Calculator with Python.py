# Project Description
# https://dailypythonprojects.substack.com/i/148415482/project-description

"""
The objective of this project is to create two Python functions -
one that calculates the area and one that calculates the perimeter of a rectangle.

1.  Create a rectangle_area function that has two parameters: width and height.
    The function should calculate the area of the rectangle and return it using a return statement.
2.  In the same script, create a rectangle_perimeter function that has two parameters: width and height. 
    The function should calculate the perimeter of the rectangle and return it using a return statement.
3.  Call the two functions by using some sample values (e.g., 10 for width and 3 for height) 
    as arguments for width and height and print out the output.

"""


def rectangle_area(width, height):
        area = width * height
        return area

def rectangle_perimeter(width, height):
        perimeter = 2 * (width + height)
        return perimeter
if __name__ == "__main__":
    width = 10
    height = 3
    ra = rectangle_area(width,height)
    print(ra)
    rp = rectangle_perimeter(width,height)
    print(rp)
