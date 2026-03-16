def check_armstrong(x):
    if x < 0:
        return False
    power = len(str(x))
    sum = 0
    temp = x
    while temp > 0:
        digit = temp % 10
        sum += digit ** power
        temp //= 10
    return sum == x


if __name__ == "__main__":
    x = int(input("Enter the number: "))
    print(check_armstrong(x))