# Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, and special characters.
import random
import string

def random_pass(pass_length):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    number = string.digits
    character = string.punctuation
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(number),
        random.choice(character)
    ]
    all_char = uppercase + lowercase + number + character
    password += random.choices(all_char,k=pass_length -4)
    random.shuffle(password)
    return "".join(password)

pass_length = int(input("Enter the length of PASSWORD: "))
result = random_pass(pass_length)
print(result)