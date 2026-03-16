def count_degit(n):
    count = 0
    while n != 0:
        n //=10
        count += 1
    return count


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print("The number of digit: ", count_degit(n))