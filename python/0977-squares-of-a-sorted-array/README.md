# 977. Squares of a Sorted Array

## Problem Summary

You are given an integer array `nums` sorted in **non-decreasing** order (ascending with possible duplicates).  
You need to:

- Square each number,
- And return a **new array** of the squares,
- Also sorted in **non-decreasing** order.

### Example 1

```text
Input:  nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Explanation:
Squares: [16, 1, 0, 9, 100]
Sorted:  [0, 1, 9, 16, 100]
```

### Example 2

```text
Input:  nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]
```

---

## Intuition

The array `nums` is already sorted, but it contains **negative numbers**.

- When you square values, **negative numbers become positive**, and their relative order by value changes.
- For example:
  - `-4` and `10` → squares are `16` and `100`, but `-4` originally comes before `10`.
  - The largest square might come from either end:
    - The most negative value (left side),
    - Or the most positive value (right side).

So, a simple approach like "square everything, then sort" would work, but:

- Squaring all values is `O(n)`,
- Sorting them again is `O(n log n)`.

We can do **better**, using the fact that the original array is already sorted.

---

## Approach: Two-Pointer from Both Ends (Fill from the Back)

Key idea:

- The **largest square** at any step will come from either:
  - The leftmost element (`nums[left]`),
  - Or the rightmost element (`nums[right]`),
  because those are the numbers with the largest absolute value.

We can:

1. Use two pointers:
   - `left = 0` → start of the array,
   - `right = n - 1` → end of the array.
2. Create a result array `result` of length `n`, initially filled with zeros.
3. We will fill `result` from **right to left** (from index `n - 1` down to `0`):
   - For each `k` from `n-1` to `0`:
     - Compute `square_left = nums[left] * nums[left]`
     - Compute `square_right = nums[right] * nums[right]`
     - The **larger** of these two should go into `result[k]`
     - Move the pointer (`left` or `right`) from which we took the larger square.

This way:

- We never sort,
- We build a sorted squared array in **one pass**,
- Time complexity stays **O(n)**,
- Extra space (besides result) is **O(1)**.

---

## Code (Python)

The code below is a LeetCode-compatible version of **your exact algorithm**.  
The only formal adjustment is adding `self` to the method signature and removing the external `print`:

```python
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given a sorted integer array nums, returns an array of the squares
        of each number, also sorted in non-decreasing order.

        :param nums: List[int] - a non-decreasing sorted array of integers
        :return: List[int] - sorted array of squared values
        """

        n = len(nums)
        result = [0] * n
        right, left = n - 1, 0

        # Fill result from the end (largest square) towards the beginning
        for k in range(n - 1, -1, -1):
            square_left = nums[left] * nums[left]
            square_right = nums[right] * nums[right]

            if square_left > square_right:
                result[k] = square_left
                left += 1
            else:
                result[k] = square_right
                right -= 1

        return result
```

- **Algorithmic logic:** exactly what you wrote.
- **Only formal changes:** `self` added for LeetCode style; no print in the core method.

---

## Step-by-Step Walkthrough

Let’s walk through your algorithm on the classic example:

```python
nums = [-4, -1, 0, 3, 10]
```

Initial setup:

- `n = 5`
- `result = [0, 0, 0, 0, 0]`
- `left = 0` (points to `-4`)
- `right = 4` (points to `10`)

We will fill `result` starting from index `k = 4` down to `0`.

---

### Iteration 1: k = 4

- `left = 0`, `right = 4`
- `nums[left] = -4`, so `square_left = 16`
- `nums[right] = 10`, so `square_right = 100`
- Compare: `16` vs `100` → `square_right` is larger

So:

- `result[4] = 100`
- Move `right` one step left: `right = 3`

Current state:

- `result = [0, 0, 0, 0, 100]`
- `left = 0`, `right = 3`

---

### Iteration 2: k = 3

- `nums[left] = -4`, `square_left = 16`
- `nums[right] = 3`, `square_right = 9`
- Compare: `16` vs `9` → `square_left` is larger

So:

- `result[3] = 16`
- Move `left` one step right: `left = 1`

Current state:

- `result = [0, 0, 0, 16, 100]`
- `left = 1` (`-1`), `right = 3` (`3`)

---

### Iteration 3: k = 2

- `nums[left] = -1`, `square_left = 1`
- `nums[right] = 3`, `square_right = 9`
- Compare: `1` vs `9` → `square_right` is larger

So:

- `result[2] = 9`
- `right -= 1` → `right = 2`

Current state:

- `result = [0, 0, 9, 16, 100]`
- `left = 1` (`-1`), `right = 2` (`0`)

---

### Iteration 4: k = 1

- `nums[left] = -1`, `square_left = 1`
- `nums[right] = 0`, `square_right = 0`
- Compare: `1` vs `0` → `square_left` is larger

So:

- `result[1] = 1`
- `left += 1` → `left = 2`

Current state:

- `result = [0, 1, 9, 16, 100]`
- `left = 2` (`0`), `right = 2` (`0`)

---

### Iteration 5: k = 0

- `left = 2`, `right = 2`
- `nums[left] = 0`, `square_left = 0`
- `nums[right] = 0`, `square_right = 0`
- `square_left` and `square_right` are equal → else-block is used

So:

- `result[0] = 0`
- `right -= 1` → `right = 1`

Final:

- `result = [0, 1, 9, 16, 100]`

Loop ends. We have the correct answer.

---

## Time and Space Complexity

### Time Complexity

- We use a single loop that iterates from `k = n - 1` down to `0`.
- Each iteration does:
  - Constant work: two multiplications, a comparison, and a couple of assignments.

So overall:

\[
\text{Time Complexity} = O(n)
\]

### Space Complexity

- We allocate a `result` array of size `n` (which is required by the problem: we must return a new array).
- Beyond that, we use only constant extra variables: `left`, `right`, `square_left`, `square_right`, `k`.

So:

\[
\text{Extra Space Complexity} = O(1) \quad (\text{excluding the required output array})
\]

---

## Edge Cases

### 1. All Non-Negative Numbers

```python
nums = [0, 1, 2, 3]
```

- The array is already non-negative and sorted.
- Squaring keeps the order non-decreasing: `[0, 1, 4, 9]`.
- Our algorithm still works:
  - `right` will always produce the largest square,
  - We fill from the back with `nums[right]^2`,
  - Result ends up sorted.

### 2. All Non-Positive Numbers

```python
nums = [-7, -5, -3, -1]
```

- After squaring: `[49, 25, 9, 1]` → sorted descending.
- But we want ascending: `[1, 9, 25, 49]`.
- Our algorithm:
  - Compares `left` (most negative) and `right` (least negative),
  - The **absolute value on the left** is larger,
  - So we fill `result` from the back with `square_left`.
- End result is correctly sorted.

### 3. Mixed Negatives and Positives

```python
nums = [-3, -1, 0, 2, 5]
```

- The two-pointer logic still correctly handles which side has the current largest absolute value.

### 4. Single Element

```python
nums = [5]        # or [-5]
```

- `n = 1`, `result = [0]`
- `k = 0`, only one iteration, either side gives the same square.
- Result: `[25]`

### 5. Empty Array

Although LeetCode typically doesn’t give empty input for this problem, logically:

```python
nums = []
```

- `n = 0`, `result = []`
- The loop doesn't run.
- We simply return `[]`.

---

## Key Takeaways

- This problem is a classic example of combining:
  - **Two-pointer technique** (left & right),
  - With **sorted array** properties.
- Instead of:
  - Squaring and sorting (`O(n log n)`),
- You can:
  - Use two pointers and fill from the back in **O(n)**.

The pattern here is extremely useful and shows up in many problems:

- Handling sorted arrays with negatives,
- Working with absolute values,
- Merging from both ends,
- Building a result array from the back when you always know the **current largest** element.
