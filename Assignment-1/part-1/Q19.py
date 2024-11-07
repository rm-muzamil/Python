# Function to check the case of a string

def check_string_case(s):
    if s.isupper():
        return "The string is uppercase."
    elif s.islower():
        return "The string is lowercase."
    elif any(c.isupper() for c in s) and any(c.islower() for c in s):
        return "The string is a mix of uppercase and lowercase."
    else:
        return "The string does not contain alphabetic characters."

string_input = input("Enter a string: ")
result = check_string_case(string_input)
print(result)
