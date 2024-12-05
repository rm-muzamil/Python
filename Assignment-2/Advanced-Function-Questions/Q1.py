# Write a function that calculates the power of a number without using the ** operator.
def power(base,exponent):
    if exponent == 0:
        return 1
    is_nagative = exponent < 0
    if is_nagative:
        exponent = -exponent
    result = 1
    for _ in range(exponent):
        result *= base
    if is_nagative:
        result = 1/result
    return result
base,exponent=float(input("Enter the base Number")),int(input("Enter the exponent"))
result = float(power(base,exponent))
print(result)

