# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
def rect_area(length, width):
    return length * width
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object
def rect_solid_area(length, width, height):
    return length * width * height
# The following four lines are just there to make the code work without errors until functions are added

# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

def surface_area(length, width, height):
    return 2 * ((length * width) + (width * height) + (length * height))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))
print("Solid Area of the rectangle: " + str(rect_solid_area(length, width, height)))