# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).////

def get_letter_grade(percentage):
    if 90 <= percentage <= 100:
        return "A"
    elif 80 <= percentage < 90:
        return "B"
    elif 70 <= percentage < 80:
        return "C"
    elif 60 <= percentage < 70:
        return "D"
    elif 0 <= percentage < 60:
        return "F"
    else:
        return "Invalid percentage. Please enter a number between 0 and 100."


percentage = float(input("Enter your grade percentage: "))
letter_grade = get_letter_grade(percentage)
print(f"Your letter grade is: {letter_grade}")
