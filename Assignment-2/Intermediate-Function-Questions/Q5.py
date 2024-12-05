# Create a function that takes a list of integers and returns the sum of all even numbers.
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
a , b = int(input("Enter the first number: ")), int(input("Enter the secound number: "))
result = gcd(a,b)
print(result)
