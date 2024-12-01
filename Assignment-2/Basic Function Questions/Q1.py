# Write a function to calculate the area of a circle given its radius.
def area_of_circle(radius):
    area = 3.14 * radius**2
    return area

radius = float(input("Enter the radius of the circle"))
result = area_of_circle(radius)
print(result)