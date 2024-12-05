# Create a function that takes a list of numbers and returns the largest number.
def is_largest(num):
    if not num:
        return None
    largest = num[0]
    for number in num:
        if number > largest:
            largest = number
    return largest
num = [21,32,93,14,56]
result = is_largest(num)
print(result)