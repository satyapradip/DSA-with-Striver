"""
================================================================================
PROBLEM: Toggle the i-th Bit of a Number
================================================================================

QUESTION:
---------
Given a number 'n' and a position 'i' (0-indexed from right), toggle (flip) the
bit at the i-th position. That means:
  - If the i-th bit is currently 0 → make it 1
  - If the i-th bit is currently 1 → make it 0

All other bits should remain unchanged.

Example:
  n = 13  (binary: 1101)
  i = 2   (0-indexed from right)
  
  Binary of 13:  1  1  0  1
                 ↑        ↑
                bit3     bit0
              bit2 ← i=2
  
  The 2nd bit (0-indexed) is currently '1'.
  After toggling it becomes '0'.
  Result: 1001 (binary) = 9 (decimal)

================================================================================
APPROACH: Using Bitwise XOR (^) with a Mask
================================================================================

KEY CONCEPT - XOR (^) Truth Table:
  A ⊕ 0 = A   (XOR with 0 keeps the bit unchanged)
  A ⊕ 1 = ¬A  (XOR with 1 FLIPS/TOGGLES the bit)

This is the magic of XOR! When you XOR a bit with 1, it flips.
When you XOR a bit with 0, it stays the same.

STEPS:
  1. Create a MASK: Left-shift 1 by 'i' positions → (1 << i)
     This creates a number where ONLY the i-th bit is 1, rest are 0.
     
     Example: i = 2
       1 << 2  =  0001 << 2  =  0100  (binary)  =  4 (decimal)
       The mask has 1 only at position 2.

  2. Apply XOR: result = n ^ (1 << i)
     - The i-th bit of n gets XOR'd with 1 → it FLIPS
     - All other bits get XOR'd with 0 → they STAY THE SAME

================================================================================
VISUAL EXAMPLE: n = 13 (1101), i = 2
================================================================================

Step 1: Create mask
  1 << 2  =  0100  (binary)

Step 2: XOR n with mask
    n     =  1 1 0 1   (13)
    mask  =  0 1 0 0   (4)
    -----------------
    XOR   =  1 0 0 1   (9)
    
    ↑ The 2nd bit (underlined) flipped from 1 → 0
    All other bits remained unchanged.

Result: 9

================================================================================
ANOTHER EXAMPLE: n = 10 (1010), i = 0
================================================================================

Step 1: Create mask
  1 << 0  =  0001  (binary)

Step 2: XOR n with mask
    n     =  1 0 1 0   (10)
    mask  =  0 0 0 1   (1)
    -----------------
    XOR   =  1 0 1 1   (11)
    
    ↑ The 0th bit flipped from 0 → 1

Result: 11

================================================================================
WHY XOR? (The Intuition)
================================================================================

Think of XOR with 1 as a "light switch":
  - If the light is OFF (0), flipping the switch turns it ON (1)
  - If the light is ON (1), flipping the switch turns it OFF (0)

XOR with 0 is like "do nothing" — the bit passes through unchanged.

This is why XOR is the PERFECT operator for toggling bits!

================================================================================
COMPARISON: Check vs Set vs Toggle
================================================================================

Operation    |  Operator  |  Mask        |  Effect
-------------|------------|--------------|-------------------------
Check bit    |  &         |  (1 << i)    |  Is it 1 or 0?
Set bit      |  |         |  (1 << i)    |  Force it to 1
Toggle bit   |  ^         |  (1 << i)    |  Flip it (0↔1)

All three use the SAME mask (1 << i) but different operators!
"""

def toggle_ith_bit(n, i):
    """
    Toggle (flip) the i-th bit of number n.
    
    Args:
        n: The input number
        i: The bit position to toggle (0-indexed from right)
    
    Returns:
        The number with the i-th bit toggled
    
    How it works:
        (1 << i) creates a mask with 1 at position i
        n ^ mask toggles only the bit at position i
    """
    return n ^ (1 << i)


# ============================================================================
# ALTERNATIVE APPROACH (Step-by-step for understanding)
# ============================================================================
def toggle_ith_bit_explained(n, i):
    """
    Same as above, but with explicit steps for learning.
    """
    # Step 1: Create the mask
    mask = 1 << i
    print(f"  Mask: 1 << {i} = {mask} (binary: {bin(mask)})")
    
    # Step 2: XOR n with the mask
    result = n ^ mask
    print(f"  {n} ^ {mask} = {result}")
    
    return result


# ============================================================================
# HELPER: Print binary representation nicely
# ============================================================================
def print_binary(n, bits=8):
    """Print a number in binary format with leading zeros."""
    return format(n, f'0{bits}b')


# ============================================================================
# MAIN - Test the function
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TOGGLE i-th BIT - EXAMPLES")
    print("=" * 60)
    
    # --- Example 1: Toggle bit 2 of 13 ---
    print("\n📌 Example 1: n = 13 (1101), i = 2")
    print("-" * 40)
    n = 13
    i = 2
    print(f"  Before: n = {n}  (binary: {print_binary(n, 4)})")
    print(f"  Toggle bit position: {i}")
    result = toggle_ith_bit_explained(n, i)
    print(f"  After:  n = {result} (binary: {print_binary(result, 4)})")
    print(f"  ✅ Bit {i} flipped from 1 → 0")
    
    # --- Example 2: Toggle bit 0 of 10 ---
    print("\n📌 Example 2: n = 10 (1010), i = 0")
    print("-" * 40)
    n = 10
    i = 0
    print(f"  Before: n = {n}  (binary: {print_binary(n, 4)})")
    print(f"  Toggle bit position: {i}")
    result = toggle_ith_bit_explained(n, i)
    print(f"  After:  n = {result} (binary: {print_binary(result, 4)})")
    print(f"  ✅ Bit {i} flipped from 0 → 1")
    
    # --- Example 3: Toggle bit 3 of 7 ---
    print("\n📌 Example 3: n = 7 (0111), i = 3")
    print("-" * 40)
    n = 7
    i = 3
    print(f"  Before: n = {n}  (binary: {print_binary(n, 4)})")
    print(f"  Toggle bit position: {i}")
    result = toggle_ith_bit_explained(n, i)
    print(f"  After:  n = {result} (binary: {print_binary(result, 4)})")
    print(f"  ✅ Bit {i} flipped from 0 → 1")
    
    # --- Example 4: Toggle back to original (XOR property) ---
    print("\n📌 Example 4: Toggle TWICE to get back original")
    print("-" * 40)
    n = 25  # 11001
    i = 3
    print(f"  Original: n = {n} (binary: {print_binary(n, 5)})")
    
    first = toggle_ith_bit(n, i)
    print(f"  1st toggle: {first} (binary: {print_binary(first, 5)})")
    
    second = toggle_ith_bit(first, i)
    print(f"  2nd toggle: {second} (binary: {print_binary(second, 5)})")
    print(f"  ✅ Toggling twice gives back the original number!")
    print(f"  🔑 This is a key property of XOR: A ^ B ^ B = A")
    
    # --- Summary ---
    print("\n" + "=" * 60)
    print("📝 SUMMARY")
    print("=" * 60)
    print("""
  Operation:  n ^ (1 << i)
  
  Why XOR?    Because XOR with 1 FLIPS the bit
              Because XOR with 0 KEEPS the bit
  
  Mask:       (1 << i)  →  puts a 1 at position i, 0 everywhere else
  
  Analogy:    XOR with 1 = light switch (flip)
              XOR with 0 = do nothing (pass through)
    """)