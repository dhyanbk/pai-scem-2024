import math

def hemisphere_area(radius):
    # Surface area of a hemisphere is given by 3 * π * r^2
    area = 3 * math.pi * radius ** 2
    return area

# Example usage:
radius = 5
area = hemisphere_area(radius)
print(f"The surface area of a hemisphere with radius {radius} is {area:.2f} square units.")