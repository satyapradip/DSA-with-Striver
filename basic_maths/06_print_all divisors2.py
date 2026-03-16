import math;
def print_all_divisors(x):
    res = []
    for i in range (1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            res.append(i)
            if i != x // i:
                res.append(x // i)
    return res


if __name__ == "__main__":
    x = int(input("Enter the number: "))
    print(print_all_divisors(x))

