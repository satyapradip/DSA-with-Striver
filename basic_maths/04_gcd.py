def gcd_of_two_number(a, b):
    if b == 0:
        return a
    else:
        return gcd_of_two_number(b, a % b)
    # gcd = 0
    # for i in range(1, min(a, b) + 1):
    #     if a % i == 0 and b % i == 0:
    #         gcd = i
    # return gcd




if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The gcd of two number is: ", gcd_of_two_number(a, b))

    