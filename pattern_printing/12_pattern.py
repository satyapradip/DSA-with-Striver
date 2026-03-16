def pattern12(n):
    for i in range(n):
        for j in range(1,i+1):
            print(j, end=" ")

            
        spaces = 2 * (n - i)
        for k in range(spaces):
            print(" ", end=" ")

        for j in range(i,0,-1):
            print(j ,end=" ")
        print() # new line after each row


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    pattern12(n)
