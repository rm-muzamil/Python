# Write a function to check whether a string is a palindrome.
def is_palindrome(string):
    reverse = string[::-1]
    if string != reverse:
        return("The given string is not palindrome")
    return("The given string is palindrome")
    

string = input("Enter the palindrome string").lower()
result = is_palindrome(string)
print(result)