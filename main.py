"""
Quentin Jaquith
CS 162
4/6/2024
"""

# Returns Area of Rectangle
def rect_area(length, width):
    return length * width

# Returns Surface Area of Rectangular Solid
def rect_surface_area(length, width, height):
    area = rect_area(length, width)
    side1area = length * height
    side2area = width * height
    surface_area = 2 * area * 2 * side1area * 2 * side2area
    return surface_area


# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))
