# Function to check if three sides form a valid triangle
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


try:
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))
    side3 = float(input("Enter the third side: "))
    
    if is_valid_triangle(side1, side2, side3):
        print("The sides form a valid triangle.")
    else:
        print("The sides do not form a valid triangle.")
except ValueError:
    print("Please enter valid numbers for the sides.")
