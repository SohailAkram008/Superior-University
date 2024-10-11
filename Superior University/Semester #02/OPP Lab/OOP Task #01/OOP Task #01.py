# Task no 01.
# revision
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number // 2)+ 1) :
        if number % i == 0:
            return False
    return True

def main():
    while True:
        user_input = input("Enter a number to check(Q to exit): ")
        if user_input.lower() == 'q':
            break
        number = int(user_input)
        if is_prime(number):
                print(f"{number} is a prime number.")
        else:
                print(f"{number} is not a prime number.")

main()