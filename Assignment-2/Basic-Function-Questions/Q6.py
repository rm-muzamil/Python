# Create a function to check if a given number is prime.

def count_vowels(string):
    string = string.lower()
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count +=1
    return count
string = input("Enter the string")
result = count_vowels(string)
print(result)