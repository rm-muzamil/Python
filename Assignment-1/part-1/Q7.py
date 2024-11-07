# Write a program to find the largest of three numbers

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return f"The largest Number is: {num1}"
    elif num2 >= num1 and num2 >= num3:
        return f"The largest Number is: {num2}"
    else:
        return f"The largest Number is: {num3}"
    
num1 = float(input("Enter a first Number: "))
num2 = float(input("Enter a secound Number: "))
num3 = float(input("Enter a third Number: "))
result = find_largest(num1, num2, num3)
print(result)