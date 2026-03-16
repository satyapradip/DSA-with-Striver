
def print_1_to_n(n):
    if n <= 0:
        return
    print_1_to_n(n-1)
    print(n)






if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print("The numbers from 1 to", n, "are:")
    print_1_to_n(n)

