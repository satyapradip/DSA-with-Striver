def pattern10(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(n-2,-1,-1):
        for j in range(i + 1):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    pattern10(n)