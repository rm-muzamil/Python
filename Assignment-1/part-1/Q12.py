# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.


def categorize_temperature(celsius):
    if celsius <= 0:
        return "The temperature is freezing."
    elif 0 < celsius < 33:
        return "The temperature is moderate."
    else:
        return "The temperature is hot."


try:
    temperature = float(input("Enter the temperature in Celsius: "))
    result = categorize_temperature(temperature)
    print(result)
except ValueError:
    print("Please enter a valid number for the temperature.")
