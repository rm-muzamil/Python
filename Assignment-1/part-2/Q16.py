# Create a program to calculate the sum of the digits of an inputted integer.

num = abs(int(input("Enter the integer")))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num //=10
print(sum)