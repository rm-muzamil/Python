# Create a function that takes a string and counts the frequency of each character.
def frequency_of_char(str):

    str = str.upper().replace(" ","")
    frequency = {}
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
str = input("Enter a string")
result = frequency_of_char(str)
print(result)