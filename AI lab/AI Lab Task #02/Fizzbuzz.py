def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def user_input():
    print("Welcome to the FizzBuzz game!")
    while True:
        user_input = input("Enter a number: ")
        if user_input.isdigit():
            n = int(user_input)
            fizzbuzz(n)
            break
        else:
            print("Invalid integer. Please try again.")
    print("Game Over!")

user_input()