# 88. Merge Sorted Array

## Problem Summary

You are given two sorted integer arrays `nums1` and `nums2`, and two integers `m` and `n`:

- `nums1` has length `m + n`.
- The **first `m` elements** of `nums1` contain the valid elements, sorted in non-decreasing order.
- The **last `n` elements** of `nums1` are placeholders (usually `0`) and should be ignored initially.
- `nums2` has length `n` and is also sorted in non-decreasing order.

Your task:

> Merge `nums2` into `nums1` as one **sorted** array, **in-place**, without returning anything.

After the function:

- `nums1` should contain the merged sorted array of length `m + n`.
- The function should **not** return a new array (must modify `nums1` in-place and return `None`).

---

## Example

```text
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output:
nums1 = [1,2,2,3,5,6]
```

- Initially, meaningful values in `nums1` are `[1, 2, 3]` (first `m` elements).
- `nums2` is `[2, 5, 6]`.
- After merging, `nums1` becomes a fully sorted array of length 6.

---

## Intuition

If we try to merge from the **front** of `nums1`, we quickly run into a problem:

- We would need to **shift** elements to make room for smaller values.
- This shifting makes the solution messy or even `O(n^2)` in the worst case.

Instead, we can use the fact that:

- `nums1` has extra space **at the end**.
- Both arrays are already **sorted**.

So a very powerful approach is to merge from the **backwards**:

- Keep three pointers:
  - `i` → last valid element in `nums1` (index `m - 1`)
  - `j` → last element in `nums2` (index `n - 1`)
  - `k` → last position in `nums1` (index `m + n - 1`)

At each step:

- Compare `nums1[i]` and `nums2[j]`.
- Put the **larger value** at `nums1[k]`.
- Move the corresponding pointer (`i` or `j`) one step to the left.
- Move `k` one step to the left.

This way, we never overwrite unprocessed values, and we use the extra space in `nums1` effectively.

---

## Approach

1. Initialize three pointers:
   - `i = m - 1` → last valid index in `nums1`
   - `j = n - 1` → last index in `nums2`
   - `k = m + n - 1` → last index in `nums1` (full size)

2. While there are still elements left in `nums2` (i.e., `j >= 0`):
   - If `i >= 0` and `nums1[i] > nums2[j]`:
     - Place `nums1[i]` at `nums1[k]`
     - Decrement `i`
   - Otherwise:
     - Place `nums2[j]` at `nums1[k]`
     - Decrement `j`
   - In both cases, decrement `k` after placing a value.

3. When the loop finishes:
   - All elements from `nums2` have been merged.
   - If `i` is still `>= 0`, the remaining elements in `nums1` are already in the correct place.

This works because we always place the **largest remaining element** at the **end** of `nums1`.

---

## Code (Python)

Your original logic is correct.  
Here is the refined version with proper `self`, no printing, and clear comments:

```python
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 as one sorted array in-place.

        Args:
            nums1: List[int] of length m + n, where the first m elements
                   are sorted and valid, and the last n elements are placeholders.
            m: Number of valid elements in nums1.
            nums2: List[int] of length n, sorted.
            n: Number of elements in nums2.

        Returns:
            None. The result is stored in nums1 in-place.
        """

        # i: last valid index in nums1
        i = m - 1
        # j: last index in nums2
        j = n - 1
        # k: last index of the merged array in nums1
        k = m + n - 1

        # Merge from the back, filling nums1 from the end
        while j >= 0:
            # If there are still elements in nums1 to compare
            # and nums1[i] is larger, place nums1[i] at nums1[k]
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                # Otherwise place nums2[j] at nums1[k]
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # No return needed, nums1 is modified in-place.
```

### Example Usage (for local testing)

> Note: On LeetCode you don't need the `if __name__ == "__main__":` part; this is only for testing locally.

```python
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    print(nums1)  # [1, 2, 2, 3, 5, 6]
```

---

## Step-by-Step Walkthrough

Let’s walk through the main example:

```text
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6],          n = 3
```

Initial pointers:

- `i = m - 1 = 2` → `nums1[i] = 3`
- `j = n - 1 = 2` → `nums2[j] = 6`
- `k = m + n - 1 = 5` → position to fill in `nums1`

### Iteration 1

- Compare `nums1[i] = 3` and `nums2[j] = 6`
- `6` is larger → set `nums1[k] = 6`
- Decrement `j` → `j = 1`
- Decrement `k` → `k = 4`

Array now:

```text
nums1 = [1, 2, 3, 0, 0, 6]
```

### Iteration 2

- `nums1[i] = 3`, `nums2[j] = 5`
- `5` is larger → `nums1[k] = 5`
- `j = 0`, `k = 3`

```text
nums1 = [1, 2, 3, 0, 5, 6]
```

### Iteration 3

- `nums1[i] = 3`, `nums2[j] = 2`
- `3` is larger → `nums1[k] = 3`
- `i = 1`, `k = 2`

```text
nums1 = [1, 2, 3, 3, 5, 6]
```

### Iteration 4

- `nums1[i] = 2`, `nums2[j] = 2`
- They are equal → we take `nums2[j]` (or `nums1[i]`, both are fine)
- `nums1[k] = 2`
- `j = -1`, `k = 1`

```text
nums1 = [1, 2, 2, 3, 5, 6]
```

Loop stops (`j < 0`):

- The merged array is fully built in `nums1`
- Final result: `[1, 2, 2, 3, 5, 6]`

---

## Time and Space Complexity

### Time Complexity

We process each element at most once:

- Each step of the loop decrements `k` (and either `i` or `j`).
- The loop runs at most `m + n` times.

\[
\text{Time Complexity} = O(m + n)
\]

### Space Complexity

We use only a few integer variables:

- `i`, `j`, `k`

No extra arrays or data structures.

\[
\text{Space Complexity} = O(1)
\]

This satisfies the **in-place** requirement.

---

## Key Takeaways

- Merging **from the end** is the key idea:
  - We avoid overwriting unprocessed values.
  - We take advantage of `nums1` having extra space at the back.
- The three-pointer pattern (`i`, `j`, `k`) is a classic trick for in-place merges.
- This question is a great example for:
  - Combining **sorted arrays**
  - Working **in-place**
  - Using **two-pointer** / **three-pointer** techniques

This pattern will appear again in more advanced problems (e.g., merging sorted lists, intervals, or K sorted arrays).

