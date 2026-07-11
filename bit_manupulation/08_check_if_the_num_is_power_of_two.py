def check_if_num_is_power_of_2(n):
  return n > 0 and (n & (n-1)) == 0


if __name__ == "__main__":
  print(check_if_num_is_power_of_2(16))