#  Write a program that checks if a given number is positive, negative, or zero.

def check_number(num):
    if num > 0:
        return "The given Number is positive."
    elif num < 0:
        return "The given Number is negative."
    else:
        return "The given Number is zero."


number = float(input("Enter a number: "))
result = check_number(number)
print(result)
