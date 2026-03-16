
def check_prime_num(x):
    cnt = 0
    if x < 2:
        return False
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
            
    return cnt == 2



if __name__ == "__main__":
    x = int(input("Enter the number: "))
    print(check_prime_num(x))