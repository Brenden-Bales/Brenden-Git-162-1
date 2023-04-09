# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object

# The following four lines are just there to make the code work without errors until functions are added
# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

# I wasnt sure how you wanted the second function to call the first, the instructions called for
# calling rect_solid_area 3 times, however that would not result in correct surface area.
# but I can do that if you'd like.
def rect_solid_area(length, width):
    return length * width


def surface_area_rect(length, width, height):
    return (length * width + length * height + width * height) * 2


rect_area = rect_solid_area(length, width)
total_surface_area = surface_area_rect(length, width, height)
print("Length = ", length, "Width = ", width, "Height = ", height)
print("rectangle area =", rect_area)
print("Total Surface Area = ", total_surface_area)
# I can modify it to add units if you would like, or I can modify to print the solid 3D volume also.
