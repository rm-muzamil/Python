# Write a function to find the factorial of a number using recursion.
def factorial(num):
    anser = 1
    while num > 0:
        anser *= num
        num -=1
    return anser
num = int(input("Enter the Number"))
result = factorial(num)
print(result)