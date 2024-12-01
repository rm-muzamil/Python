# Create a program that simulates a countdown timer starting from a given number down to zero.
import time
start = int(input("Enter the starting number:"))
for i in range(start,-1,-1):
    print(i)
    time.sleep(1)
print("Timer Completed")