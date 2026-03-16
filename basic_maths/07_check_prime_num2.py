def check_prime_num(x):

    for i in range(3, int(x**0.5) + 1, 2):  # Only check odd numbers
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    x = int(input("Enter the number: "))
    print(check_prime_num(x))