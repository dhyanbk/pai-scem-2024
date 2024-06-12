def calculate_rectangle_area(length, width):
    return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_rectangle_area(length, width)
print("The area of the rectangle is:", area)
