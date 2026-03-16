def pattern7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for k in range(2*i+1):
            print("*", end=" ")
        for l in range(n-i-1):
            print(" ",end=" ")
        print() # new line after each row


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    pattern7(n)
