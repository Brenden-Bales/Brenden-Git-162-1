def rect_area(length, width):
    area = length * width
    return area

def rect_surface_area(length, width, height):
    lw = rect_area(length,width)
    return (lw * height)

