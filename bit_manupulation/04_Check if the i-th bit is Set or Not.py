# Approach 1: Using Left Shift (1 << i) and Bitwise AND (&)
# To check the i-th bit (0-indexed) of a number 'n':
# 1. Create a mask: Left-shift 1 by 'i' positions (1 << i). This generates a number with only the i-th bit set to 1.
#    Example: For i=2, mask is 1 << 2 = 0100 (binary).
# 2. Perform bitwise AND: (n & (1 << i)).
#    - If the result is non-zero, it means the i-th bit in 'n' was also 1 (set).
#    - If the result is zero, it means the i-th bit in 'n' was 0 (not set).
def checkIthBit(n, i):
  if (n & (1<<i)) != 0:
    return True
  else:
    return False
  
if __name__ == "__main__":
  print(checkIthBit(13, 2))



# Approach 2: Using Right Shift (n >> i) and Bitwise AND (& 1)
# To check the i-th bit (0-indexed) of a number 'n':
# 1. Right-shift 'n' by 'i' positions (n >> i). This moves the i-th bit to the 0-th (least significant) position.
#    Example: For n=13 (1101 binary), i=2: 13 >> 2 = 0011 (decimal 3). The original 2nd bit (1) is now at the 0th position.
# 2. Perform bitwise AND with 1: ((n >> i) & 1). This isolates the 0-th bit.
#    - If the result is 1, the i-th bit was set.
#    - If the result is 0, the i-th bit was not set.
def checkIthBit2(n, i):
  if (n >> i) & 1 == 0:
    return False
  else:
    return True