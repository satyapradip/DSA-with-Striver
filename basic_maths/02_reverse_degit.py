def reverse_degit(n):
    rev = 0
    while n != 0:
        degit = n % 10
        rev = rev *10 + degit
        n //= 10
    return rev


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print("The reverse number is: ", reverse_degit(n))