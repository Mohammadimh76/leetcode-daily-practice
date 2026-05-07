# 27. Remove Element

## Problem Summary

You are given an integer array `nums` and an integer `val`.

Your task is to **remove all occurrences** of `val` in-place from the array `nums` and return the **number of elements remaining** after removal.

- The **relative order** of the remaining elements **does not need to be preserved** (but our solution does preserve it).
- You must do this using **O(1) extra space**.
- After the function returns:
  - The first `k` elements of `nums` should contain the elements that are **not equal** to `val`.
  - The value of `k` is the number returned by the function.
  - Anything after index `k - 1` can be ignored.

**Example**

```text
Input:  nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

Here:

- `k = 2`
- The first two elements of `nums` are `[2, 2]`
- Values after index `1` do not matter and are denoted by `_`.

---

## Intuition

We want to **filter out** all elements equal to `val` from the array **in-place**, without using any extra array.

A clean way to do this is using a **two-pointer** idea:

- Use one pointer to **scan** the array (`i` → the fast pointer).
- Use another pointer to track the **position where we should write** the next valid element (`k` → the slow pointer, or "write index").

The idea:

- Start `k` at `0`.
- Iterate through all indices `i` from `0` to `len(nums) - 1`:
  - If `nums[i]` is **not equal** to `val`, this is a *valid* element:
    - Write it at index `k` → `nums[k] = nums[i]`
    - Move `k` forward (`k += 1`)
  - If `nums[i] == val`, we simply **skip** it.

At the end:

- All elements that are **not equal** to `val` will be stored in `nums[0..k-1]`.
- The value `k` is the number of remaining elements.

---

## Approach

1. **Initialize a write index `k`**

   - Set `k = 0`.
   - This pointer marks the position where the next valid element should be written.

2. **Loop through the array with index `i`**

   - For each `i` from `0` to `len(nums) - 1`:
     - If `nums[i] != val`:
       - Copy this element to the current `k` position: `nums[k] = nums[i]`.
       - Increment `k` by `1`.

3. **Ignore elements equal to `val`**

   - Whenever `nums[i] == val`, we do nothing:
     - We do **not** increment `k`.
     - We do **not** write that value anywhere.
   - Effectively, all occurrences of `val` are skipped and overwritten by later valid elements (if any).

4. **Return `k`**

   - `k` is the count of elements that are **not equal** to `val`.
   - Only the first `k` elements of `nums` are considered valid after the function finishes.

---

## Code (Python)

Your original code is correct and optimal.  
Below is the same logic with some small comments and an example usage.

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k is the "write index" (slow pointer)
        k = 0
        
        # i is the "read index" (fast pointer)
        for i in range(len(nums)):
            # If current element is not equal to val, keep it
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # k is the number of elements that are not equal to val
        return k

# Time: O(n)
# Space: O(1)
```

### Example Usage

```python
if __name__ == "__main__":
    nums = [3, 2, 2, 3, 4, 3, 5]
    val = 3
    
    sol = Solution()
    k = sol.removeElement(nums, val)
    
    print("k =", k)                  # number of elements not equal to val
    print("filtered nums =", nums[:k])  # only first k elements are valid
```

Possible output:

```text
k = 4
filtered nums = [2, 2, 4, 5]
```

The contents of `nums[k:]` (after index `k - 1`) are not important.

---

## Example Walkthrough

Let’s walk through the algorithm on this input:

```text
nums = [3, 2, 2, 3, 4], val = 3
```

Initial:

- `k = 0`
- We will scan `i` from `0` to `4`.

Step-by-step:

1. `i = 0`, `nums[0] = 3`
   - `nums[0] == val` → skip  
   - `k` stays `0`

2. `i = 1`, `nums[1] = 2`
   - `nums[1] != val` → keep it  
   - `nums[0] = 2`  
   - `k = 1`  
   - Array becomes: `[2, 2, 2, 3, 4]`

3. `i = 2`, `nums[2] = 2`
   - `nums[2] != val` → keep it  
   - `nums[1] = 2`  
   - `k = 2`  
   - Array: `[2, 2, 2, 3, 4]` (no visible change)

4. `i = 3`, `nums[3] = 3`
   - `nums[3] == val` → skip  
   - `k` stays `2`

5. `i = 4`, `nums[4] = 4`
   - `nums[4] != val` → keep it  
   - `nums[2] = 4`  
   - `k = 3`  
   - Array becomes: `[2, 2, 4, 3, 4]`

End:

- `k = 3`
- First `k` elements: `nums[:3] = [2, 2, 4]`
- All occurrences of `3` have been removed in-place.

---

## Time and Space Complexity

- **Time Complexity**:  
  We iterate through the array once:

  \[
  O(n)
  \]

  where \( n \) is the length of `nums`.

- **Space Complexity**:  
  We use only a couple of integer variables (`k` and `i`):

  \[
  O(1)
  \]

  This satisfies the **in-place** and **constant extra space** requirements.

---

## Key Points

- This is a classic **two-pointer (fast & slow)** problem.
- `k` (slow pointer) tracks **where to write** the next valid element.
- `i` (fast pointer) scans all elements.
- All elements equal to `val` are skipped.
- Only the first `k` elements in `nums` are guaranteed to be valid after the function returns.
