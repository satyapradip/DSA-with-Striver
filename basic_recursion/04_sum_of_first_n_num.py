def sum_of_first_n_natural_numbers(n):
    if n <= 0:
        return 0
    return n + sum_of_first_n_natural_numbers(n-1)


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print("The sum of first", n, "natural numbers is:", sum_of_first_n_natural_numbers(n))