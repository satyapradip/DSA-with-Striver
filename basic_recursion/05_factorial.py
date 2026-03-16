def factorial_of_n(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial_of_n(x-1)


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(factorial_of_n(n))