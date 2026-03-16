def pattern4(n):
    for i in range(1,n+1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()   # new line after each row


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    pattern4(n)
