# Function to check if a string is a palindrome

def is_palindrome(st):

    st = st.replace(" ", "").lower()

    return st == st[::1]


string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
