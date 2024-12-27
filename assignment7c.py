def is_prime_number():
    number = int(input("Enter a number: "))
    if number <= 1:
        print(f"{number} is not a prime number.")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return
    print(f"{number} is a prime number.")

is_prime_number()
