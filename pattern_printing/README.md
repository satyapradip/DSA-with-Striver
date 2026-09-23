# Pattern Printing

Pattern printing is a compact way to practice nested loops. Most interview questions in this topic are solved by deciding three things for every row:

1. How many rows are required?
2. How many spaces, symbols, or numbers belong in the current row?
3. What value should be printed at each column?

The files in this folder use `n` as the input size. Unless stated otherwise, the running time is `O(n^2)` because the output itself can contain that many characters, and the extra space is `O(1)` apart from the output buffer used by the console.

## Core Method

Use the outer loop for rows and one or more inner loops for the parts of a row:

```python
for row in range(number_of_rows):
    # print spaces
    # print stars or numbers
    print()
```

Useful row formulas:

| Part of row | Common formula |
| --- | --- |
| Growing triangle | `row + 1` |
| Shrinking triangle | `n - row` |
| Pyramid spaces | `n - row - 1` |
| Pyramid symbols | `2 * row + 1` |
| Diamond | pyramid followed by inverted pyramid |
| Alternating value | `value = 1 - value` |

## Pattern Index

| File | Pattern | Main idea |
| --- | --- | --- |
| [`01_pattern.py`](01_pattern.py) | Solid square | Fixed number of rows and columns |
| [`02_pattern.py`](02_pattern.py) | Increasing star triangle | Print `row + 1` stars |
| [`03_pattern.py`](03_pattern.py) | Increasing number triangle | Print `1` through `row + 1` |
| [`04_pattern4.py`](04_pattern4.py) | Repeated-row number triangle | Print the row number repeatedly |
| [`05_pattern5.py`](05_pattern5.py) | Decreasing star triangle | Print `n - row` stars |
| [`06_pattern6.py`](06_pattern6.py) | Decreasing number triangle | Print a decreasing number of values |
| [`07_pattern.py`](07_pattern.py) | Pyramid | Spaces on both sides and odd star count |
| [`08_pattern.py`](08_pattern.py) | Inverted pyramid | Reverse the pyramid row order |
| [`09_pattern.py`](09_pattern.py) | Diamond | Pyramid plus inverted pyramid |
| [`10_pattern.py`](10_pattern.py) | Double triangle | Growing triangle plus shrinking triangle |
| [`11_pattern.py`](11_pattern.py) | Binary triangle | Alternate `1` and `0` in each row |
| [`12_pattern.py`](12_pattern.py) | Palindromic number pattern | Increasing numbers, spaces, decreasing numbers |

## Pattern Details

### 1. Solid Square - `01_pattern.py`

For an input of `4`:

```text
* * * *
* * * *
* * * *
* * * *
```

**Method:** Run both loops exactly `n` times. The row does not affect the number of columns.

```python
for row in range(n):
    for column in range(n):
        print("*", end=" ")
    print()
```

**Interview point:** This is the base case for nested-loop output. When every row has the same width, both loop bounds are fixed.

### 2. Increasing Star Triangle - `02_pattern.py`

```text
*
* *
* * *
* * * *
```

**Method:** On zero-based row `row`, print `row + 1` stars. The inner-loop bound grows with the outer-loop index.

**Interview point:** Recognize the relationship between the row number and the number of items in that row.

### 3. Increasing Number Triangle - `03_pattern.py`

```text
1
1 2
1 2 3
1 2 3 4
```

**Method:** The row controls the length, while the column controls the value. Print `column + 1` for every column from `0` through `row`.

### 4. Repeated-Row Number Triangle - `04_pattern4.py`

```text
1
2 2
3 3 3
4 4 4 4
```

**Method:** Print the one-based row number `row` exactly `row` times. Unlike pattern 3, the value does not change across a row.

**Interview point:** Separate the concepts of loop count and printed value. They are often controlled by different variables.

### 5. Decreasing Star Triangle - `05_pattern5.py`

```text
* * * *
* * *
* *
*
```

**Method:** Start with `n` stars and reduce the count by one after every row. With a zero-based row, the count is `n - row`.

### 6. Decreasing Number Triangle - `06_pattern6.py`

The conventional interview version is:

```text
1 2 3 4
1 2 3
1 2
1
```

**Method:** The number of values is `n - row`, and each row starts at `1`.

**Current file note:** The current code uses `range(1, n + 1)` for `i` and `range(1, n - i + 1)` for `j`. Therefore, for input `4`, it prints rows containing `3`, `2`, `1`, and `0` values. To implement the conventional version, use a zero-based row and `range(1, n - row + 1)`.

### 7. Pyramid - `07_pattern.py`

```text
      *
    * * *
  * * * * *
* * * * * * *
```

**Method:** Each row has three sections:

- `n - row - 1` leading spaces
- `2 * row + 1` stars
- `n - row - 1` trailing spaces, if fixed-width alignment is required

The odd number of stars keeps the pyramid centered.

**Interview point:** Split a visually complex row into independent sections instead of trying to calculate everything in one loop.

### 8. Inverted Pyramid - `08_pattern.py`

```text
* * * * * * *
  * * * * *
    * * *
      *
```

**Method:** Iterate from `n - 1` down to `0`. The star count is still `2 * row + 1`, but the row values are visited in reverse order.

### 9. Diamond - `09_pattern.py`

```text
      *
    * * *
  * * * * *
* * * * * * *
  * * * * *
    * * *
      *
```

**Method:** Combine two shapes:

1. A normal pyramid for rows `0` through `n - 1`.
2. An inverted pyramid for rows `n - 2` through `0`.

Starting the second half at `n - 2` prevents printing the widest middle row twice.

**Interview point:** Reuse the same row formulas and change only the direction of traversal.

### 10. Double Triangle - `10_pattern.py`

```text
*
* *
* * *
* * *
* *
*
```

**Method:** Print an increasing triangle, then print a decreasing triangle beginning at `n - 2`. Skipping the repeated largest row avoids a duplicate at the center.

### 11. Binary Triangle - `11_pattern.py`

```text
1
0 1
1 0 1
0 1 0 1
```

**Method:** Start each row with `1` on odd-numbered rows and `0` on even-numbered rows. After every print, toggle the value with:

```python
value = 1 - value
```

This works because `1 - 1` is `0` and `1 - 0` is `1`.

**Interview point:** Decide whether the alternating sequence should restart on every row or continue globally. This pattern restarts it on every row.

### 12. Palindromic Number Pattern - `12_pattern.py`

The intended shape is:

```text
1      1
1 2    2 1
1 2 3  3 2 1
1 2 3 4 4 3 2 1
```

**Method:** Build each row from three parts:

1. Increasing values from `1` to `row`.
2. A shrinking block of middle spaces.
3. Decreasing values from `row` back to `1`.

The row stays visually symmetric because both number halves use the same row limit.

**Interview point:** Symmetric patterns are easiest when the left and right halves are generated separately. Avoid special cases for individual rows.

## Interview Checklist

When given an unfamiliar pattern:

1. Write the expected output for `n = 3` or `n = 4`.
2. Count the items in every row.
3. Decide whether each count grows, shrinks, or stays fixed.
4. Separate spaces, symbols, and numbers into distinct loops.
5. Choose zero-based or one-based indexing and keep it consistent.
6. Check the first row, middle row, and last row for off-by-one errors.
7. Avoid printing an extra center row when joining two shapes.
8. Keep `print()` for the newline and `end=" "` for values on the same row.

## Complexity

For an `n` by `n`-sized pattern, the output normally takes `O(n^2)` time. The loops use `O(1)` auxiliary space when values are printed directly instead of collected in a list.

## Running a Pattern

From this folder, run any script with Python and enter `n` when prompted:

```powershell
python .\02_pattern.py
```
