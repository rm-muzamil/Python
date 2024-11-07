# Take an integer and check if it’s even or odd.

def check_integer(num):
    if (num % 2 == 0):
        return "The given Number is even"
    else:
        return "The given Number is odd"
    
number = int(input("Enter a Number: "))
result = check_integer(number)
print(result)