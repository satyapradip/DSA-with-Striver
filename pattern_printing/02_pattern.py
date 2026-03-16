def pattern2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()   # new line after each row


if __name__ == "__main__":
    n = int(input())
    pattern2(n)
