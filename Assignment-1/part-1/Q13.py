# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Infinity"
        else:
            return num1 / num2
    else:
        return "Invalid Operator"
    
num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the secound Number: "))
operator = input("Enter an operator from given (+, -, *, /) ")
result = calculate(num1,num2,operator)
print(result)