# Print the sum of even and odd numbers separately up to a given number.
num = int(input("Enter the Number"))
even = 0
odd = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print("sum of all even number",even,"sum of odd number",odd)