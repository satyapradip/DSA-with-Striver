def print_n_to_1(n):
    if n <= 0:
        return
    print(n)
    print_n_to_1(n-1)


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print("The numbers from", n, "to 1 are:")
    print_n_to_1(n)