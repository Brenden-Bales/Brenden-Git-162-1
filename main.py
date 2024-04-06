"""
Logan Chance
CS 162
4/6/2024
"""

# Project requires TWO functions:

# Returns Area of Rectangle

# Returns Surface Area of Rectangular Solid

# Returns Solid Area of Rectangle

# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))
print("Solid Area of the rectangle: " + str(rect_solid_area(length, width, height)))
