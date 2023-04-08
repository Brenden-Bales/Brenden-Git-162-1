
input("welcome to the first python code of spring '23 cs162")
print()


length = int(input("enter the length of the object as a positive integer: "))
width = int(input("enter the width of the object as a positive integer: "))
height = int(input("enter the height of the object as a positive integer: "))
print()


def rect_solid_area(length, width, height):
    area = length * width
    print ("the area of your rectangle is: ", area)

def surface_area(length, width, height):
    surface_area = (2 * length * height) + (2 * length + width) + (2 * width * height)
    return surface_area

rect_solid_area(length, width, height)
surface_area(length, width, height)


print()
print("length = ", length, "width = ", width, "height = ", height)
print("total surface area = ", surface_area(length, width, height))

## surface area = 2lh + 2lw + 2wh
## volume = lwh