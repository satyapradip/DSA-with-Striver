# Basic Maths for DSA

Welcome, learner. This folder is your foundation course in the mathematical building blocks behind Data Structures and Algorithms. You will not master advanced DSA without fluency in these core number-theoretic ideas: digit manipulation, primality, divisors, GCD, and special numbers.

Treat each file here as a standalone lesson. Read the code, trace it on paper with a small input, then run it and break it.

## Learning Objectives

By the end of this module you should be able to:

- Extract digits from an integer using modulo and division.
- Reverse a number and detect palindromes without converting to strings.
- Compute the Greatest Common Divisor (GCD) using the Euclidean algorithm.
- Identify Armstrong numbers.
- Enumerate all divisors of a number in O(sqrt(n)) time.
- Test primality efficiently (O(sqrt(n))).
- Analyze time and space complexity of number-theoretic routines.

## Folder Contents

| File | Concept | Key Technique | Complexity |
|------|---------|---------------|------------|
| `01_count_digits.py` | Count digits in an integer | Repeated integer division by 10 | O(log₁₀ n) time, O(1) space |
| `01_count_digit2.py` | Count digits (math approach) | `log10(n) + 1` | O(1) time, O(1) space |
| `02_reverse_degit.py` | Reverse digits of a number | `rev = rev * 10 + (n % 10)` | O(log₁₀ n) time, O(1) space |
| `03_check_palindrome.py` | Check if a number is a palindrome | Reverse-and-compare | O(log₁₀ n) time, O(1) space |
| `04_gcd.py` | Greatest Common Divisor | Euclidean algorithm (recursive) | O(log min(a, b)) time |
| `05_check_armstrong.py` | Check Armstrong number | Digit power sum | O(log₁₀ n) time |
| `06_print_all_divisors.py` | Print all divisors (brute force) | Linear scan 1..n | O(n) time |
| `06_print_all divisors2.py` | Print all divisors (optimized) | Scan up to sqrt(n), add pairs | O(sqrt(n)) time |
| `07_check_prime_num.py` | Check primality (basic) | Count divisors up to n | O(n) time |
| `07_check_prime_num2.py` | Check primality (optimized) | Check up to sqrt(n), skip evens | O(sqrt(n)) time |

---

## Lesson 1 — Counting Digits

### The Idea

To count digits of a positive integer `n`, repeatedly remove the last digit using integer division by 10 (`n //= 10`) until `n` becomes 0. Each removal counts as one digit.

### Walkthrough

`n = 123`
1. `123 // 10 = 12`, count = 1
2. `12 // 10 = 1`, count = 2
3. `1 // 10 = 0`, count = 3
Result: **3 digits**

### Mathematical Shortcut

The number of digits in `n` is `floor(log10(n)) + 1`. See `01_count_digit2.py`.

### Edge Cases

- `n = 0` → the loop body never runs; return 0 unless you explicitly handle it. Decide your convention upfront.
- Negative numbers → take `abs(n)` first if you want to count digits ignoring the sign.

### Complexity

- Time: O(log₁₀ n) — one iteration per digit.
- Space: O(1).

---

## Lesson 2 — Reversing a Number

### The Idea

Build the reversed number digit by digit:
1. Extract the last digit: `digit = n % 10`.
2. Append it to the result: `rev = rev * 10 + digit`.
3. Remove the processed digit: `n //= 10`.
4. Repeat until `n == 0`.

### Walkthrough

`n = 123`
| Step | n | digit | rev |
|------|---|-------|-----|
| 1 | 123 | 3 | 0*10+3 = 3 |
| 2 | 12 | 2 | 3*10+2 = 32 |
| 3 | 1 | 1 | 32*10+1 = 321 |
Result: **321**

### Why This Matters

Digit reversal is a primitive used in palindrome checking, certain string/number problems, and interview questions on digit DP.

### Complexity

- Time: O(log₁₀ n)
- Space: O(1)

---

## Lesson 3 — Palindrome Check

### The Idea

A number is a palindrome if it reads the same backward as forward. Reverse the number (Lesson 2) and compare with the original.

### Walkthrough

`x = 121`
- `temp = 121`, `rev` built = 121
- `rev == temp` → **True**

`x = -121` → return `False` immediately (negative sign breaks symmetry).

### Walkthrough `x = 10`
- `rev` built = 1 (not 01, because leading zeros vanish in integers)
- `1 != 10` → **False**

### Complexity

- Time: O(log₁₀ x)
- Space: O(1)

---

## Lesson 4 — Greatest Common Divisor (GCD)

### The Idea

The GCD of two integers `a` and `b` is the largest integer that divides both without remainder.

### The Euclidean Algorithm (the efficient way)

```
gcd(a, b) = gcd(b, a % b)
base case: gcd(a, 0) = a
```

Why it works: any common divisor of `a` and `b` must also divide `a % b` (since `a = q*b + r`, so `r = a - q*b`). The problem shrinks rapidly.

### Walkthrough

`gcd(48, 18)`
1. `gcd(48, 18)` → `gcd(18, 48 % 18 = 12)`
2. `gcd(18, 12)` → `gcd(12, 18 % 12 = 6)`
3. `gcd(12, 6)` → `gcd(6, 12 % 6 = 0)`
4. `gcd(6, 0)` → return **6**

### Brute Force (for contrast)

Loop `i` from 1 to `min(a, b)`, track the largest `i` dividing both. O(min(a, b)) — too slow for large inputs. The commented block in `04_gcd.py` shows this approach.

### Complexity

- Time: O(log min(a, b)) — each step reduces the problem significantly.
- Space: O(log min(a, b)) recursion stack, or O(1) if written iteratively.

---

## Lesson 5 — Armstrong Numbers

### The Idea

An Armstrong number (narcissistic number) of `d` digits equals the sum of its digits each raised to the power `d`.

```
153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153  → Armstrong
```

### Algorithm

1. Count digits `d = len(str(x))` (or use the digit-counting logic).
2. For each digit, add `digit^d` to a running sum.
3. Return `sum == x`.

### Walkthrough `x = 153`
- `d = 3`
- digits: 3, 5, 1
- sum = 3³ + 5³ + 1³ = 27 + 125 + 1 = 153
- `153 == 153` → **True**

### Complexity

- Time: O(log₁₀ x) to extract digits + O(d) power operations — effectively O(log x).
- Space: O(1).

---

## Lesson 6 — Printing All Divisors

### Brute Force (`06_print_all_divisors.py`)

Loop `i` from 1 to `x`. If `x % i == 0`, `i` is a divisor.

- Time: O(n)
- Simple but slow for large `n`.

### Optimized (`06_print_all divisors2.py`)

Divisors come in pairs. If `i` divides `x`, then `x // i` also divides `x`. Only scan up to `sqrt(x)`:

```python
for i in range(1, int(sqrt(x)) + 1):
    if x % i == 0:
        add i
        if i != x // i:   # avoid double-counting perfect squares
            add x // i
```

### Walkthrough `x = 36`, sqrt = 6
- `i=1`: 36%1==0 → add 1, add 36
- `i=2`: add 2, add 18
- `i=3`: add 3, add 12
- `i=4`: add 4, add 9
- `i=6`: 36%6==0 → add 6; `i == x//i` (6==6), so do NOT add again
Result: `[1, 36, 2, 18, 3, 12, 4, 9, 6]` (sort if you need order)

### Complexity

- Time: O(sqrt(n))
- Space: O(number of divisors) for the result list.

---

## Lesson 7 — Primality Testing

### Basic (`07_check_prime_num.py`)

A prime has exactly two divisors: 1 and itself. Count all divisors from 1 to `x`; if count == 2, it's prime.

- Time: O(n)
- Space: O(1)

### Optimized (`07_check_prime_num2.py`)

Key insights:
1. Numbers `< 2` are not prime.
2. You only need to check divisors up to `sqrt(x)`. If `x = a * b` and both `a, b > sqrt(x)`, then `a * b > x`, contradiction.
3. After handling 2, skip even numbers (check only odd `i` starting from 3, step 2).

```python
if x < 2: return False
if x == 2: return True
if x % 2 == 0: return False
for i in range(3, int(x**0.5) + 1, 2):
    if x % i == 0: return False
return True
```

### Complexity

- Time: O(sqrt(n))
- Space: O(1)

### Common Pitfall

`07_check_prime_num2.py` as written returns `True` for `x = 1` and even numbers > 2 because it lacks the `x < 2` and `x % 2 == 0` guards. Always test edge cases: 0, 1, 2, 3, 4, 9, 25.

---

## Study Roadmap (Tutor's Recommended Order)

1. `01_count_digits.py` → `01_count_digit2.py` (iteration vs. math)
2. `02_reverse_degit.py` (digit extraction primitive)
3. `03_check_palindrome.py` (apply reversal)
4. `04_gcd.py` (recursion + number theory)
5. `05_check_armstrong.py` (digit power sum)
6. `06_print_all_divisors.py` → `06_print_all divisors2.py` (O(n) → O(sqrt n) optimization lesson)
7. `07_check_prime_num.py` → `07_check_prime_num2.py` (primality optimization)

## Practice Checklist

Before moving on, make sure you can do these without looking at the code:

- [ ] Count digits of any positive integer using `while n > 0`.
- [ ] Reverse a number and explain what happens to trailing zeros.
- [ ] Check palindrome for both positive and negative inputs.
- [ ] Compute GCD of two numbers by hand using Euclidean algorithm, then verify with code.
- [ ] List all Armstrong numbers between 1 and 1000.
- [ ] Print divisors of 100 in sorted order using the sqrt method.
- [ ] Test primality for 1, 2, 97, 100, and explain why each result is correct.

## How to Run

Each script is self-contained. Run from the `basic_maths` folder:

```bash
python 01_count_digits.py
python "06_print_all divisors2.py"
```

You will be prompted to enter a number. Trace the output by hand first, then compare.

## Next Steps

After mastering this folder, proceed to:
- **Bit Manipulation** — for low-level number tricks (XOR, bit masks).
- **Basic Hashing** — for frequency counting in number problems.
- **Recursion** — GCD here is recursive; deepen that skill.

---

*"Math is not about memorizing formulas. It is about recognizing patterns and reducing a big problem to a smaller one you already know how to solve." — Keep tracing, keep breaking, keep building.*