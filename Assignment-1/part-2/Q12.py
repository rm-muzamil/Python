# Print all prime numbers between 1 and 50.
for i in range(2,51):
    prime = True
    for j in range(2, int(i**0.5)+1):
     if i % j == 0:
        prime = False
        break
    if prime:
        print(i,end=" ")