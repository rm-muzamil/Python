# print the multiplication table of the given number

def table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
        
num = int(input("Enter the number:"))
result = table(num)
print(result)