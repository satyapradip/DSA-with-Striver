"""
================================================================================
Problem: Remove the Last Set Bit (Turn off the rightmost 1-bit)
================================================================================

Given a positive integer 'n', we need to remove (unset / turn off) the 
rightmost set bit (the last '1' bit) in its binary representation.

In other words: Given n, find n' such that n' = n with its rightmost 1-bit
changed to 0.

--------------------------------------------------------------------------------
Example 1:
    Input:  n = 12
    Binary: n   = 1100
            n'  = 1000    (rightmost 1-bit at position 2 is removed)
    Output: 8

Example 2:
    Input:  n = 10
    Binary: n   = 1010
            n'  = 1000    (rightmost 1-bit at position 1 is removed)
    Output: 8

Example 3:
    Input:  n = 7
    Binary: n   = 0111
            n'  = 0110    (rightmost 1-bit at position 0 is removed)
    Output: 6

Example 4:
    Input:  n = 8
    Binary: n   = 1000
            n'  = 0000    (only 1-bit is removed)
    Output: 0

Example 5:
    Input:  n = 16
    Binary: n   = 10000
            n'  = 00000
    Output: 0
--------------------------------------------------------------------------------

================================================================================
Approach 1: Using n & (n - 1)  [OPTIMAL - O(1) time]
================================================================================

The expression n & (n - 1) is a VERY FAMOUS bit manipulation trick.

Key Insight — What happens when we subtract 1 from a number?

When we subtract 1 from a number:
  - The rightmost 1-bit becomes 0
  - All bits to the RIGHT of that rightmost 1-bit become 1

Examples:
  n      = 12  →  binary: 1100
  n - 1  = 11  →  binary: 1011
  
  n      = 10  →  binary: 1010
  n - 1  = 9   →  binary: 1001

  n      = 7   →  binary: 0111
  n - 1  = 6   →  binary: 0110

  n      = 8   →  binary: 1000
  n - 1  = 7   →  binary: 0111

Now, if we do n & (n - 1):
  - Bits LEFT of the rightmost 1-bit remain unchanged (because they're same in both)
  - The rightmost 1-bit becomes 0 (because in n-1 it's 0)
  - Bits RIGHT of the rightmost 1-bit become 0 (because in n they're 0)

Example step-by-step:
  n        = 12  =  1 1 0 0
  n-1      = 11  =  1 0 1 1
  -----------------------------
  n & (n-1)=  8  =  1 0 0 0    ← Rightmost 1-bit removed!

------------------------------------------------------------------
Visual Illustration:

    n        = 1 1 0 0  (12)
              ↓ ↓ ↓ ↓
    n-1      = 1 0 1 1  (11)
    ─────────────────────
    n & (n-1)= 1 0 0 0  (8)
              ↑ ↑ ↑ ↑
              │ │ │ └── 0 & 1 = 0  (bits right of rightmost 1)
              │ │ └──── 0 & 1 = 0  (rightmost 1-bit → 0)
              │ └────── 1 & 0 = 0  (bits right of rightmost 1)
              └──────── 1 & 1 = 1  (bits left of rightmost 1 unchanged)
------------------------------------------------------------------

Time Complexity:  O(1)
Space Complexity: O(1)

================================================================================
Approach 2: Using n - (n & -n)  [Alternative - also O(1)]
================================================================================

This uses the concept of isolating the rightmost set bit.

The expression (n & -n) isolates (extracts) the rightmost set bit.
Then we simply subtract it from n.

  - n & -n  →  gives the value of the rightmost set bit alone
  - n - (n & -n)  →  removes that bit

Example:
  n = 12  =  1100
 -n = -12 =  0100  (2's complement representation)
  n & -n  =  0100  = 4  (isolated rightmost set bit)
  n - 4   =  8     ✓

How 2's complement works:
  -n = ~n + 1
  n     = 1100
  ~n    = 0011  (bitwise NOT)
  ~n+1  = 0100  (2's complement of 12 = -12)

So n & -n = 1100 & 0100 = 0100 = 4 ✓

Time Complexity:  O(1)
Space Complexity: O(1)
"""


# ==============================================================================
# IMPLEMENTATION 1: Using n & (n - 1)  [MOST OPTIMAL & COMMONLY USED]
# ==============================================================================

def remove_last_set_bit_using_n_and_n_minus_1(n: int) -> int:
    """
    Removes the rightmost set bit using the n & (n-1) trick.
    
    This is the most elegant and widely-used approach in competitive programming.
    
    Args:
        n: A positive integer
        
    Returns:
        Integer with the rightmost 1-bit turned off
    """
    return n & (n - 1)


# ==============================================================================
# IMPLEMENTATION 2: Using n - (n & -n)
# ==============================================================================

def remove_last_set_bit_using_isolation(n: int) -> int:
    """
    Removes the rightmost set bit by first isolating it using n & -n,
    then subtracting it from the original number.
    
    This approach is useful when you also need the VALUE of the 
    rightmost set bit (isolated bit).
    
    Args:
        n: A positive integer
        
    Returns:
        Integer with the rightmost 1-bit turned off
    """
    # Isolate the rightmost set bit
    rightmost_set_bit = n & -n
    # Subtract it to remove it
    return n - rightmost_set_bit


# ==============================================================================
# Helper function: Visualize the process
# ==============================================================================

def visualize_removal(n: int) -> None:
    """
    Prints a step-by-step visualization of removing the last set bit.
    """
    print(f"{'='*50}")
    print(f"Number: {n}")
    print(f"Binary: {n:08b}")
    print(f"{'='*50}")
    
    result = remove_last_set_bit_using_n_and_n_minus_1(n)
    
    print(f"\nUsing n & (n-1):")
    print(f"  n      = {n:08b}  ({n})")
    print(f"  n-1    = {n-1:08b}  ({n-1})")
    print(f"  {'─'*20}")
    print(f"  Result = {result:08b}  ({result})")
    
    # Alternative approach visualization
    rightmost = n & -n
    result2 = remove_last_set_bit_using_isolation(n)
    
    print(f"\nUsing n - (n & -n):")
    print(f"  n               = {n:08b}  ({n})")
    print(f"  -n (2's comp)   = {-n & 0xFF:08b}  ({-n})")
    print(f"  n & -n (isolated)= {rightmost:08b}  ({rightmost})")
    print(f"  {'─'*20}")
    print(f"  n - isolated    = {result2:08b}  ({result2})")
    
    print(f"\n{'='*50}")
    
    
# ==============================================================================
# Test the function
# ==============================================================================
if __name__ == "__main__":
    test_cases = [12, 10, 7, 8, 16, 1, 0, 15, 20, 31, 100, 255]
    
    print(f"\n{'='*60}")
    print(f"{'n':<10} {'Binary':<12} {'After removal':<18} {'Result (int)'}")
    print(f"{'='*60}")
    
    for n in test_cases:
        result = remove_last_set_bit_using_n_and_n_minus_1(n)
        print(f"{n:<10} {n:08b}          {result:08b}           {result:<10}")
    
    print(f"\n{'='*60}")
    
    # Visualize a few examples in detail
    visualize_removal(12)
    visualize_removal(10)
    visualize_removal(7)