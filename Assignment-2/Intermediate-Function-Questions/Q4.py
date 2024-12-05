# Create a function that takes a list of integers and returns the sum of all even numbers.
def sum_of_even(numbers):
    sum_of_all_even_nums = 0
    for i in numbers:
        if i % 2 == 0:
            sum_of_all_even_nums += i
    return sum_of_all_even_nums
numbers = [1,2,3,4,5,6,7,8,9,0]
result = sum_of_even(numbers)
print(result)