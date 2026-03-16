def print_all_divisors(x):
    res = []
    for i in range (1, x+1):
        if x % i == 0:
            res.append(i)
    return res


if __name__ == "__main__":
    x = int(input("Enter the number: "))
    print(print_all_divisors(x))