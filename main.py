# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
def rect_area(length, width):
    return length * width
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object
def rect_surface_area(length, width, height):
    front_area = rect_area(length, height)
    side_area = rect_area(width, height)
    top_area = rect_area(length, width)
    return 2 * (front_area + side_area + top_area)

# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

surface_area = rect_surface_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)
