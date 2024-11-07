# Write a program to check if a number is within a specified range

def is_number_in_the_range(num, min_range, max_range):
    if min_range <= num <= max_range:
        return f"{num} is in the range of {min_range} to {max_range}"
    else:
        return "The given number is not in the range"
    
num = float(input("Enter the Number: "))
min_range = float(input("Enter the MINIMUM range Number: "))
max_range = float(input("Enter the MAXIMUM range Number: "))
result = is_number_in_the_range(num, min_range, max_range)
print(result)