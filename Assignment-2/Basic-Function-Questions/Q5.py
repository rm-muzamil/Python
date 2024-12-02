# Create a function to check if a given number is prime.
def is_the_number_prime_or_not(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
num = int(input("Enter the Prime Number"))
result = is_the_number_prime_or_not(num)
print(result)