# Function to determine age category
def age_category(age):
    if age < 18:
        return "You are a minor."
    elif 18 <= age < 45:
        return "You are an adult."
    else:
        return "You are a senior citizen."

age = int(input("Enter your age: "))
result = age_category(age)
print(result)
