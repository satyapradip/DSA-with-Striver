def find_nth_fibonacci(n):
  if n <= 1:
    return n
  return find_nth_fibonacci(n-1) + find_nth_fibonacci(n-2)

if __name__ == "__main__":
  print(find_nth_fibonacci(7))