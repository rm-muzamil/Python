# Function to check if a number is a multiple of both 3 and 5
def is_multiple_of_3_and_5(num):
    return num % 3 == 0 and num % 5 == 0


try:
    number = int(input("Enter a number: "))
    if is_multiple_of_3_and_5(number):
        print(f"{number} is a multiple of both 3 and 5.")
    else:
        print(f"{number} is not a multiple of both 3 and 5.")
except ValueError:
    print("Please enter a valid integer.")
