# Write a program that continues to ask for a number until the correct number is guessed.
guessed_num = 5
num = 0
while num != guessed_num:
    num = int(input("guess a number"))
    