# Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.
def temperature_converter(input_value):
    temp = ""
    scale = ""
    input_value = input_value.replace(" " , "")
    for char in input_value:
        if char.isdigit():
            temp += char
        else:
            scale += char
    temp = int(temp)
    scale = scale[0].lower()
    if scale == "f":
        result = f"{(temp - 32) * 5/9} C"
    else:
        result = f"{(temp * 9/5) + 32} F"
    return result
input_value = input("Enter the temperature (like 32 C or 104 F): ")
result = temperature_converter(input_value)
print(result)