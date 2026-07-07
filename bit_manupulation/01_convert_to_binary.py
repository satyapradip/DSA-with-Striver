def decimal_to_binary(n):
  result = ""
  while n> 0:
    if n % 2 == 0:
      result = "0" + result
    else:
      result = "1" + result
    n = n // 2
  return result

if __name__ == "__main__":
  print(decimal_to_binary(10))