# Write a function to find the nth Fibonacci number using recursion.
def fibonacci(nth_term):
    first_fib = 0
    secound_fib = 1

    while nth_term > 0:
        final = 0
        fina = secound_fib + first_fib
        final += fina
        first_fib = final
        nth_term-=1
    return final
nth_term = int(input("Enter the nth term"))
result = fibonacci(nth_term)
print(result)