def print_name_n_times(name, n):
    if n <= 0:
        return
    print(name)
    print_name_n_times(name, n-1)


if __name__ == "__main__":
    name = input("Enter the name: ")
    n = int(input("Enter the number of times: "))
    print_name_n_times(name, n)