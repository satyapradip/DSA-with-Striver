def pattern5(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()   # new line after each row


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    pattern5(n)
