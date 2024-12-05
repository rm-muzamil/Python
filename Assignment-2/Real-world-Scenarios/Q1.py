# Write a function that takes a list of employee salaries and calculates the average salary.
def avg_salary(salaries):
    len_of = len(salaries)
    sum_of = sum(salaries)
    avg = sum_of / len_of
    return avg
print(avg_salary({12000,15600,13435,14500}))