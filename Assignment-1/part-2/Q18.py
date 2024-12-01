# Use a loop to print numbers in reverse order within a given range.
start = int(input("Enter the starting range"))
end = int(input("Enter the end range"))

for i in range(end, start - 1,-1):
    print(i)