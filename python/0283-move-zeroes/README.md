# 283. Move Zeroes

## Problem Summary

You are given an integer array `nums`. Your task is to:

> Move all the `0`s to the **end** of the array, while **keeping the relative order of the non-zero elements the same**.

The operation must be done:

- **In-place** (modify `nums` directly)
- With **minimum extra operations**
- Without returning a new array

### Example 1

```text
Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

Explanation:

- The non-zero elements `[1, 3, 12]` keep their relative order.
- All zeros are moved to the end.

### Example 2

```text
Input:  nums = [0]
Output: [0]
```

---

## Intuition

We want to:

1. Keep all **non-zero elements** in their original relative order.
2. Push all **zeros** to the **end**.
3. Do it **in-place** (no extra array).

A simple but inefficient idea would be:

- Remove all zeros
- Count how many zeros there were
- Append that many zeros at the end

But this usually requires extra space or multiple passes and is not as clean.

A better way is to use a **two-pointer technique**:

- One pointer scans the array (`j`).
- Another pointer tracks where the **next non-zero** element should go (`i`).

Whenever we find a non-zero element at `j`:

- We **swap** it with the element at `i`.
- Then we move `i` forward.

This way:

- All non-zero elements are compacted at the **front** of the array.
- All zeros naturally end up at the **back**.
- The relative order of non-zero elements is preserved.

---

## Approach

We use two indices:

- `i` — the position where the **next non-zero** element should be placed.
- `j` — the current index used to scan through the array.

Steps:

1. Initialize `i = 0`.
2. Loop `j` from `0` to `len(nums) - 1`:
   - If `nums[j]` is **non-zero**:
     - Swap `nums[i]` and `nums[j]`.
     - Increment `i` (move the "non-zero boundary" forward).
3. When the loop ends:
   - All non-zero elements are at the front, in the same order as before.
   - All zeros are at the end.

Note:  
If `i == j` and `nums[j]` is non-zero, the swap is effectively a **no-op** (we swap an element with itself), which is safe and keeps the code simple.

---

## Code (Python)

The logic in this solution is based on the code you wrote.  
The only adjustment for LeetCode is to include `self` in the method signature.

```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0  # position to place the next non-zero element

        # j scans through the array
        for j in range(len(nums)):
            # When we find a non-zero element,
            # we move it to index i (if needed) and move i forward.
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
```

This matches your algorithm exactly, with the correct method signature for LeetCode.

---

## Example Walkthrough

Let’s walk through the main example:

```text
nums = [0, 1, 0, 3, 12]
```

Initial:

- `i = 0`
- `j` will iterate from `0` to `4`

### Step 1: `j = 0`

- `nums[j] = nums[0] = 0`
- It is zero → do nothing
- `i` stays `0`

Array: `[0, 1, 0, 3, 12]`

### Step 2: `j = 1`

- `nums[1] = 1` (non-zero)
- Swap `nums[i]` and `nums[j]` → swap `nums[0]` and `nums[1]`

```text
nums = [1, 0, 0, 3, 12]
i = 1
```

### Step 3: `j = 2`

- `nums[2] = 0`
- Zero → do nothing, `i` stays `1`

Array: `[1, 0, 0, 3, 12]`

### Step 4: `j = 3`

- `nums[3] = 3` (non-zero)
- Swap `nums[i]` and `nums[j]` → swap `nums[1]` and `nums[3]`

```text
nums = [1, 3, 0, 0, 12]
i = 2
```

### Step 5: `j = 4`

- `nums[4] = 12` (non-zero)
- Swap `nums[i]` and `nums[j]` → swap `nums[2]` and `nums[4]`

```text
nums = [1, 3, 12, 0, 0]
i = 3
```

Loop ends.

Final result:

```text
nums = [1, 3, 12, 0, 0]
```

- All non-zero elements `[1, 3, 12]` are in the same relative order as the original.
- All zeros are moved to the end.

---

## Time and Space Complexity

### Time Complexity

We do a **single pass** through the array:

- The index `j` runs from `0` to `n - 1`, where `n = len(nums)`.
- Each element is visited once.
- Swaps are `O(1)`.

\[
\text{Time Complexity} = O(n)
\]

### Space Complexity

We use only:

- Two integer variables: `i` and `j`.

We do not allocate any extra array or data structure.

\[
\text{Space Complexity} = O(1)
\]

This satisfies the **in-place** requirement.

---

## Edge Cases

1. **All zeros**

   ```text
   nums = [0, 0, 0]
   ```

   - The condition `nums[j] != 0` is never true.
   - `i` stays at `0`.
   - Array remains `[0, 0, 0]` — already correct.

2. **No zeros**

   ```text
   nums = [1, 2, 3]
   ```

   - Every element is non-zero.
   - For each `j`, we swap `nums[i]` with `nums[j]`.
   - But here `i == j` at every step, so we are effectively swapping each element with itself.
   - The array stays `[1, 2, 3]`.

3. **Zeros at the end already**

   ```text
   nums = [1, 2, 3, 0, 0]
   ```

   - Non-zero part is already at the front.
   - The algorithm will perform self-swaps for `j = 0,1,2`, then ignore zeros.
   - The final array remains `[1, 2, 3, 0, 0]`.

4. **Single element**

   ```text
   nums = [0]   -> [0]
   nums = [5]   -> [5]
   ```

   Both are handled correctly by the loop.

---

## Key Takeaways

- The **two-pointer pattern** (`i` and `j`) is very powerful for in-place array transformations.
- Using `i` as the "position of next non-zero" lets us:
  - Compact non-zero values at the front
  - Preserve their relative order
  - Automatically push zeros to the back
- The solution is:
  - **In-place**
  - **O(n)** time
  - **O(1)** extra space

This problem is a classic example of how to restructure an array in-place while respecting order constraints.
