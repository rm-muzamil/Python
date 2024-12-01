# Print the reverse of a given number.


# num = int(input("Enter the integer: "))
# reverse = 0
# sign = -1 if num < 0 else 1
# num = abs(num)
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10

# reverse *= sign
# print(reverse)


num = input("Enter the integer")
reverse = num[::-1] if num[0] != '-' else '-' + num[:0:-1]
print(reverse)

