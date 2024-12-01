# Write a program that breaks the loop when a certain condition is met.
while True:
    user_input = input("Enter the word: (type 'stop' to end the loop)")
    if user_input.lower() == "stop":
        print("loop ended")
        break
    print(f"you entered the word: {user_input} ")