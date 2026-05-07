# 26. Remove Duplicates from Sorted Array

## Problem Summary

You are given a sorted integer array `nums` (in non-decreasing order).

Your task is to **remove duplicate elements in-place** so that each unique value appears **only once** in the array.

- The relative order of the elements must be **preserved**.
- You must use **O(1) extra space** (modify `nums` directly).
- After removing duplicates, return the **number of unique elements** `k`.

The online judge will then check only the **first `k` elements** of `nums`.  
Everything after index `k - 1` can be ignored.

**Example**

```text
Input:  nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

Explanation:

- `k = 2`
- The first `k` elements (indices `0` and `1`) are `[1, 2]`
- Values after index `k - 1` are irrelevant and can be anything (denoted by `_`).

---

## Intuition

The array is already **sorted**, which is the main advantage here:

- All duplicates appear **next to each other**.
- This means, when we scan the array from left to right, any time we see a value that is **different from the last unique value**, we know it is a **new unique element**.

We can use the classic **two-pointers** technique:

- Pointer `i`:
  - Tracks the **position of the last unique element** in the array.
- Pointer `j`:
  - Scans the array from left to right.

For each position `j`:

- If `nums[j] != nums[i]`, we found a **new** unique value.
  - Increase `i` by 1.
  - Copy `nums[j]` into `nums[i]`.

At the end:

- All unique elements are stored in the range `nums[0..i]`.
- The number of unique elements is `i + 1`.

---

## Approach

1. **Handle empty array**

   If `nums` is empty, there are no elements to process:

   ```python
   if not nums:
       return 0
   ```

2. **Initialize pointer `i`**

   - Start `i` at index `0`.
   - This represents the index of the **last unique element** found so far.

3. **Scan with pointer `j`**

   - Start `j` from index `1` (the second element).
   - For each `j` in `[1 .. len(nums) - 1]`:
     - Compare `nums[j]` with `nums[i]`.
     - If they are **different**, we found a new unique value:
       - Move `i` forward (`i += 1`).
       - Write this new value at position `i` → `nums[i] = nums[j]`.

4. **Return the count**

   After the loop:

   - The last unique index is `i`.
   - The number of unique elements is `i + 1`.

---

## Code (Python)

Your algorithm is correct and optimal.  
The only fix needed is how the method is called. Below is the cleaned-up version with a proper usage example.

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the array is empty, there are no unique elements.
        if not nums:
            return 0
        
        # i points to the position of the last unique element.
        i = 0
        
        # j scans through the array starting from index 1.
        for j in range(1, len(nums)):
            # When we find a new value (different from nums[i]),
            # we move i forward and copy nums[j] into nums[i].
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements is i + 1
        return i + 1


if __name__ == "__main__":
    nums = [1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    
    print("k =", k)                 # number of unique elements
    print("unique part =", nums[:k])  # first k elements are the unique values
```

> Important:
> ```python
> Solution.removeDuplicates([1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5])
> ```
> is not valid, because `removeDuplicates` is an **instance method**, not a static method.  
> You correctly implemented the logic, but to call it, you must create an instance:  
> `sol = Solution()` and then `sol.removeDuplicates(nums)`.

---

## Example Walkthrough

Let’s trace the algorithm on this input:

```text
nums = [1, 1, 1, 2, 2, 3]
```

- Initial:
  - `i = 0`
  - `nums[i] = 1`

- `j = 1`:
  - `nums[1] = 1` → same as `nums[i] = 1` → **duplicate** → skip

- `j = 2`:
  - `nums[2] = 1` → same as `nums[i] = 1` → **duplicate** → skip

- `j = 3`:
  - `nums[3] = 2` → different from `nums[i] = 1` → **new unique**
  - `i += 1` → `i = 1`
  - `nums[1] = 2`
  - Array becomes: `[1, 2, 1, 2, 2, 3]`

- `j = 4`:
  - `nums[4] = 2` → same as `nums[i] = 2` → **duplicate** → skip

- `j = 5`:
  - `nums[5] = 3` → different from `nums[i] = 2` → **new unique**
  - `i += 1` → `i = 2`
  - `nums[2] = 3`
  - Array becomes: `[1, 2, 3, 2, 2, 3]`

End of loop:

- `i = 2`
- Number of unique elements: `k = i + 1 = 3`
- Unique part of the array: `nums[:k] = [1, 2, 3]`

Anything after index `2` can be ignored.

---

## Time and Space Complexity

- **Time Complexity**:  
  We traverse the array once with pointer `j`, so:
  \[
  O(n)
  \]
  where \( n \) is the length of `nums`.

- **Space Complexity**:  
  We only use a few extra variables (`i`, `j`), so:
  \[
  O(1)
  \]
  extra space (in-place modification).

---

## Key Takeaways

- This is a classic **two-pointer** problem.
- We exploit the fact that the array is **sorted**, so duplicates are adjacent.
- We maintain a **"unique prefix"** of the array in `nums[0..i]`.
- Only the first `k` elements (where `k` is the return value) are guaranteed to be valid unique values.
