# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

def check_the_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "The given sides of triangle is equilateral triangle"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return "The given sides of triangle is isoscales triangle"
    else:
        return "The given sides of triangle is scalene triangle"

side1 = float(input("Enter the First side of triangle: "))
side2 = float(input("Enter the Secound side of triangle: "))
side3 = float(input("Enter the Third side of triangle: "))
result = check_the_triangle(side1, side2, side3)
print(result)
        