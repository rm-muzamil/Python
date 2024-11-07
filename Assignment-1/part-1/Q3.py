# Write a program that checks if a given year is a leap year


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."


try:
    year = int(input("Enter a year: "))
    result = is_leap_year(year)
    print(result)
except ValueError:
    print("Please enter a valid integer for the year.")
