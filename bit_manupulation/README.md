# Bit Manipulation

Bit manipulation is the act of algorithmically manipulating the bits (0s and 1s) that represent data in a computer. Every number is stored as a sequence of bits, and bit operations are often much faster than regular arithmetic operations.

## Why Learn Bit Manipulation?

1. **Speed** - Bit operations are processed by the CPU in a single cycle.
2. **Memory** - You can pack many flags/values into a single integer.
3. **Tricks** - Many problems have elegant one-line bit solutions.
4. **Interviews** - Frequently asked in coding interviews (DSA).

## Binary Number System

We normally use decimal (base-10): 0,1,2,3,4,5,6,7,8,9
Computers use binary (base-2): 0, 1

Each binary digit is called a BIT. 8 bits = 1 byte.

Example:
    Decimal 5  ->  Binary 0101
    (because 0*8 + 1*4 + 0*2 + 1*1 = 5)

    Decimal 13 ->  Binary 1101
    (because 1*8 + 1*4 + 0*2 + 1*1 = 13)

In Python, you can see the binary form using `bin()`:
    bin(5)  ->  '0b101'       (0b prefix means "binary")
    bin(13) ->  '0b1101'

## The Six Bitwise Operators

| Operator | Name        | Example  | Result | Use                              |
|----------|-------------|----------|--------|----------------------------------|
| &        | AND         | 12 & 10  | 8      | masking/checking bits            |
| \|       | OR          | 12 \| 10 | 14     | setting bits                     |
| ^        | XOR         | 12 ^ 10  | 6      | toggling/finding unique elements |
| ~        | NOT         | ~5       | -6     | flipping bits                    |
| <<       | Left Shift  | 5 << 2   | 20     | multiply by 2^n                  |
| >>       | Right Shift | 20 >> 2  | 5      | divide by 2^n                    |

### Truth Tables

**AND (&)**: 1 only if both bits are 1
- 1 & 1 = 1
- 1 & 0 = 0
- 0 & 1 = 0
- 0 & 0 = 0

**OR (|)**: 1 if at least one bit is 1
- 1 | 1 = 1
- 1 | 0 = 1
- 0 | 1 = 1
- 0 | 0 = 0

**XOR (^)**: 1 if bits are different
- 1 ^ 1 = 0
- 1 ^ 0 = 1
- 0 ^ 1 = 1
- 0 ^ 0 = 0

**NOT (~)**: Flips all bits. In Python, `~x = -(x+1)`.

**Left Shift (<<)**: Shifts bits left, multiplies by 2^n.
**Right Shift (>>)**: Shifts bits right, divides by 2^n.

## Common Bitmask Formulas

```python
# Get i-th bit:        (n >> i) & 1            OR   n & (1 << i)
# Set i-th bit:        n | (1 << i)
# Clear i-th bit:      n & ~(1 << i)
# Toggle i-th bit:     n ^ (1 << i)
# Clear rightmost bit: n & (n - 1)
# Is power of two:     n > 0 and (n & (n - 1)) == 0
# Is even:             (n & 1) == 0
# Is odd:              (n & 1) == 1
```

## XOR Properties (Very Important)

- `a ^ a = 0`       (same numbers cancel)
- `a ^ 0 = a`       (XOR with 0 does nothing)
- XOR is commutative & associative (order doesn't matter)
- => XOR all elements; pairs cancel, unique element remains

## Folder Contents

| File | Topic |
|------|-------|
| `basics.py` | Comprehensive introduction to all 6 bitwise operators and 10 common tricks |
| `01_convert_to_binary.py` | Convert decimal integer to binary (4 approaches) |
| `02_binary_to_decimal.py` | Convert binary string to decimal (3 approaches) |
| `03_swap_two_num.py` | Swap two numbers without temp variable using XOR |
| `04_Check if the i-th bit is Set or Not.py` | Check if i-th bit is set (2 approaches) |
| `05_set_the_ith_bit.py` | Set the i-th bit to 1 using OR |
| `06_toggle_ith_bit.py` | Toggle (flip) the i-th bit using XOR |
| `07_remove_the_last_set_bit.py` | Remove the rightmost set bit using n & (n-1) |
| `08_check_if_the_num_is_power_of_two.py` | Check if a number is a power of two |
| `09_count_the_number_of_set_bits.py` | Count set bits (5 approaches, including Kernighan's) |
| `10_Minimum Bit Flips to Convert Number.py` | Min bit flips to convert start to goal |
| `11_devide_two_num.py` | Divide two integers without *, /, % using bit shifting |
| `12_Single Number.py` | Find the unique element in an array of pairs (XOR) |
| `13_subsets.py` | Generate all subsets (power set) using bit manipulation |

## Practice Problems

Try these classic problems to reinforce your understanding:

1. **Single Number** (LeetCode 136) - find unique in pairs
2. **Number of 1 Bits** (LeetCode 191) - count set bits
3. **Power of Two** (LeetCode 231) - check power of two
4. **Missing Number** (LeetCode 268) - XOR approach
5. **Single Number II** (LeetCode 137) - appears 3 times except one
6. **Reverse Bits** (LeetCode 190)
7. **Subsets** (LeetCode 78) - generate power set
8. **Divide Two Integers** (LeetCode 29) - divide without *, /, %
9. **Minimum Bit Flips** (LeetCode 2220) - XOR + count set bits

## Running the Files

Each file can be run independently:

```bash
python bit_manupulation/basics.py
python bit_manupulation/01_convert_to_binary.py
python bit_manupulation/02_binary_to_decimal.py
# ... and so on
```