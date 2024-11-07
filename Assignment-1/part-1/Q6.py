# Write a program to find the largest of two numbers.

def find_largest(num1, num2):
    if num1 > num2:
        return f"The largest number is: {num1}"
    elif num2 > num1:
        return f"The largest number is: {num2}"
    else:
        return "Both numbers are equal."


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = find_largest(num1, num2)
print(result)
