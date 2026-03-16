def fibonacci(n):
    if n <= 1:
        return n
    last = fibonacci(n-1)
    slast = fibonacci(n-2)

    return last + slast

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(fibonacci(n))