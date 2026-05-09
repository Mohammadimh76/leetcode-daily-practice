# LeetCode 167 — Two Sum II (Input Array Is Sorted)

## Problem Summary
You are given a **1-indexed** array `numbers` that is sorted in **non-decreasing** order, and an integer `target`.

Find **two numbers** such that they add up to `target`, and return their **indices (1-indexed)** as a list `[index1, index2]` where:

- `1 <= index1 < index2 <= len(numbers)`
- Exactly one solution exists (per problem statement).

You must use **constant extra space**.

---

## Key Idea (Intuition)
Because the array is sorted, we can use **two pointers**:

- `left` starts at the beginning (small values)
- `right` starts at the end (large values)

At each step we compute:

`sum_target = numbers[left] + numbers[right]`

Then:

- If `sum_target == target` → we found the answer.
- If `sum_target < target` → we need a larger sum, so move `left` rightward.
- If `sum_target > target` → we need a smaller sum, so move `right` leftward.

This works efficiently because sorting gives us a monotonic way to adjust the sum.

---

## Approach (Two Pointers)
1. Initialize:
   - `left = 0`
   - `right = len(numbers) - 1`
2. While `left < right`:
   - Compute `sum_target = numbers[left] + numbers[right]`
   - Compare with `target`:
     - Equal → return `[left + 1, right + 1]` (convert to 1-indexed)
     - Smaller → `left += 1`
     - Larger → `right -= 1`

---

## Corrected Code (LeetCode-Compatible)

> Your algorithm is correct.  
> The only required fix for LeetCode submission is adding `self` to the method signature (class-instance method requirement).  
> The core logic is unchanged.

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0

        while left < right:
            sum_target = numbers[left] + numbers[right]

            if sum_target == target:
                return [left + 1, right + 1]
            elif sum_target < target:
                left += 1
            else:
                right -= 1
```

---

## Walkthrough Example

Input:

```text
numbers = [2, 7, 11, 15], target = 9
```

- `left=0 (2)`, `right=3 (15)` → sum = 17 > 9 → move `right` to 2
- `left=0 (2)`, `right=2 (11)` → sum = 13 > 9 → move `right` to 1
- `left=0 (2)`, `right=1 (7)` → sum = 9 == 9 → return `[1, 2]`

Output:

```text
[1, 2]
```

---

## Why This Is Correct (Proof Sketch)

Because the array is sorted:

- If `numbers[left] + numbers[right]` is **too small**, increasing `left` is the only way to potentially increase the sum (moving `right` left would only decrease it).
- If the sum is **too large**, decreasing `right` is the only way to reduce the sum (moving `left` right would only increase it).

Thus, each pointer move discards impossible pairs without missing the valid solution.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`Each pointer (`left` and `right`) moves at most `n` steps total.
- **Space Complexity:** `O(1)`
  Only a few variables are used.

---

## Edge Cases

- Minimal length array: `numbers = [a, b]` (always one solution).
- Negative numbers and zero are handled naturally.
- Duplicates are fine (array is non-decreasing).
- Large values: safe in Python (no overflow issues).

---

## Notes for Local Testing

On LeetCode, you do **not** need `print(...)`. If you want to test locally:

```python
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # [1, 2]
```
