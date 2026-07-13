# Single Number

# `a ^ a = 0` (self-cancellation)
# `a ^ 0 = a` (identity)

def SingleNumber(arr):
  n = 0
  for i in  arr:
    n ^= i 
  return n

if __name__ == "__main__":
  print(SingleNumber([1, 3, 3, 2, 2]))