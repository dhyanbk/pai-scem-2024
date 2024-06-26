import math

def cylinder_area(radius, height):
    # Surface area of a cylinder is given by 2 * π * r * (r + h)
    area = 2 * math.pi * radius * (radius + height)
    return area

# Example usage:
radius = 5
height = 10
area = cylinder_area(radius, height)
print(f"The surface area of a cylinder with radius {radius} and height {height} is {area:.2f} square units.")