# CS 162

# Write a function named "rect_area" that computes the area of a rectangle. This function will take 2 parameters - length and width.
def rect_area(length, width):
    return length * width

# Write a second function named "rect_surface_area" that calls the first function - "rect_area" - to compute the surface area of a rectangular solid.
# This function will take three parameters - length, width and height.
def rect_surface_area(length, width, height):
     return 2(rect_area(length, width) + (height * length) + (height * width))

# Finds The solid area of a rectangle
def rect_solid_area(length, width, height):
    return length * width * height


