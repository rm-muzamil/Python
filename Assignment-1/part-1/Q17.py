# Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

def is_number_divisible(num):
    if num % 2 == 0 and num % 3 == 0:
        return f"The number {num} is divisible by both 2 and 3"
    elif num % 2 == 0:
        return f"The number {num} is divisible by only 2"
    elif num % 3 == 0:
        return f"The number {num} is divisible by only 3"
    else:
        return f"The number {num} is divisible nither 2 nor 3"
    
num = int(input("Enter the number"))
result = is_number_divisible(num)
print(result)
        