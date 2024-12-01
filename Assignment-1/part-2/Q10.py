# Use a loop to count the number of digits in an integer.
count = 0
num = int(input("Enter the integer:"))
num = abs(num)
while num >0:
    num //= 10
    count += 1

print("test",count)