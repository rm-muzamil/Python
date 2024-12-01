# Use nested loops to print a pyramid pattern of *
row = 5
for i in range(1,row + 1):
    for j in range(row -i):
        print(" ", end=" " )

    for k in range(i*2 - 1):
        print("*",end=" ")
    print()