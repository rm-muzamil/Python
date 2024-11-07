# Function to check if a character is a vowel or consonant

def check_vowel_or_consonant(char):
    char = char.lower()
    vowels = "aeiou"
    if len(char) == 1 and char.isalpha():
        if char in vowels:
            return "The character is a vowel."
        else:
            return "The character is a consonant."
    else:
        return "Please enter a single alphabetic character."


character = input("Enter a single character: ")
result = check_vowel_or_consonant(character)
print(result)
