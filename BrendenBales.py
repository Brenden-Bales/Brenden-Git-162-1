#Function 1
def rect_area(x, y):
    area = x * y
    return area

def rect_surface_area(l, w, h):
    surface = (rect_area(l, w) + rect_area(w, h) + rect_area(l, h))*2
    return surface
# Returns Surface Area of Rectangular Solid
# Request the dimension of a solid rectangular object

length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))
