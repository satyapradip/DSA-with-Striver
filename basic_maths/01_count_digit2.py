import math;

def count_digit(n):
    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.

    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    count = int(math.log10(n) + 1)

    return count


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print("The number of digit: ", count_digit(n))