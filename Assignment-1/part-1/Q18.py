# Function to determine pass or fail

def check_pass_fail(score):
    if score >= 50:
        return "You passed!"
    else:
        return "You failed."


score = float(input("Enter your score: "))
result = check_pass_fail(score)
print(result)
