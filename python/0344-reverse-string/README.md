# 344. Reverse String

## Problem Summary

You are given a character array `s`, where:

- `s` is a list of characters (e.g., `["h", "e", "l", "l", "o"]`).
- You need to **reverse the array in-place**.

> Do not return a new array.  
> You must modify the input array directly, using **O(1)** extra memory.

### Example 1

```text
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

### Example 2

```text
Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

---

## Intuition

We want to reverse the characters in the array **in-place**:

- The first character should swap with the last.
- The second character should swap with the second last.
- And so on, until we reach the middle of the array.

The most natural way to achieve this is using the **two-pointer technique**:

- One pointer starts from the **left** (`left`).
- Another pointer starts from the **right** (`right`).
- We swap the characters at these two pointers, then move them towards each other.

We stop when `left` meets or crosses `right`.  
At that point, the entire array is reversed.

---

## Approach

1. Initialize two indices:
   - `left = 0` (start of the array)
   - `right = len(s) - 1` (end of the array)

2. While `left < right`:
   - Swap `s[left]` and `s[right]`.
   - Move `left` forward: `left += 1`
   - Move `right` backward: `right -= 1`

3. When the loop finishes:
   - All characters are reversed **in-place**.
   - No extra array is used.

This directly satisfies the constraints:

- In-place modification
- O(1) extra space
- O(n) time

---

## Code (Python)

Below is the corrected and LeetCode-compatible version of your code.  
The algorithm is exactly the same as what you wrote; we only:

- Add `self` to the method signature.
- Remove the `print` statement (LeetCode checks the modified `s`, not printed output).

```python
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the input list of characters in-place.

        :param s: List of characters representing a string
        :return: None (modifies s in-place)
        """

        left, right = 0, len(s) - 1

        # Move two pointers towards the center
        while left < right:
            # Swap the characters at left and right
            s[left], s[right] = s[right], s[left]

            # Move pointers inward
            left += 1
            right -= 1
```

- **Logic:** exactly your logic.
- **Only changes:** method signature (`self`) + removal of `print`.

---

## Example Walkthrough

Let’s walk through the first example:

```python
s = ["h","e","l","l","o"]
```

Initial state:

- `left = 0` (points to `"h"`)
- `right = len(s) - 1 = 4` (points to `"o"`)

Array: `["h", "e", "l", "l", "o"]`

### Step 1

- `left = 0`, `right = 4`
- `s[left] = "h"`, `s[right] = "o"`

Swap:

```text
s[0], s[4] = s[4], s[0]
s = ["o", "e", "l", "l", "h"]
```

Move pointers:

```text
left = 1
right = 3
```

### Step 2

- `left = 1`, `right = 3`
- `s[1] = "e"`, `s[3] = "l"`

Swap:

```text
s[1], s[3] = s[3], s[1]
s = ["o", "l", "l", "e", "h"]
```

Move pointers:

```text
left = 2
right = 2
```

### Step 3

- `left = 2`, `right = 2`
- Now `left` is **not less than** `right` (`left == right`).

The loop condition `while left < right` fails, and we stop.

Final array:

```text
["o", "l", "l", "e", "h"]
```

The string is successfully reversed in-place.

---

## Time and Space Complexity

### Time Complexity

We:

- Use two pointers that move towards each other.
- Each character is visited at most once in a swap.
- The loop runs approximately `n / 2` iterations, where `n` is the length of `s`.

Therefore:

\[
\text{Time Complexity} = O(n)
\]

### Space Complexity

We:

- Use only a constant number of extra variables (`left`, `right`, and a temporary value during swap handled by tuple assignment).

No additional data structures are created.

\[
\text{Space Complexity} = O(1)
\]

This matches the problem’s requirement of **in-place** reversal with **constant extra space**.

---

## Edge Cases

1. **Empty array**

   ```python
   s = []
   ```

   - `len(s) = 0`, so `right = -1`
   - `left = 0`, `right = -1`
   - The condition `left < right` is false from the start.
   - The loop never runs; the array remains empty, which is correct.

2. **Single character**

   ```python
   s = ["a"]
   ```

   - `left = 0`, `right = 0`
   - `left < right` is false
   - No swaps are needed
   - The array remains `["a"]`

3. **Two characters**

   ```python
   s = ["a", "b"]
   ```

   - `left = 0`, `right = 1`
   - Swap: `["b", "a"]`
   - Then `left = 1`, `right = 0`
   - Loop ends; result is correct.

4. **Palindrome string**

   ```python
   s = ["r","a","c","e","c","a","r"]
   ```

   - Reversing a palindrome gives the same sequence.
   - Algorithm still runs, but final array equals the initial one.
   - Shows the algorithm does not rely on any special structure.

---

## Key Takeaways

- This problem is a classic example of the **two-pointer** technique:
  - One pointer from the left
  - One pointer from the right
  - Swap and move inward
- It reinforces the concept of:
  - **In-place** array manipulation
  - **O(1)** extra space
  - Clean, simple loops without unnecessary overhead
- Patterns you practice here are applicable to many other problems:
  - Reversing parts of arrays or strings
  - Palindrome checks
  - Two-pointer traversals from both ends

A clear, simple, and correct solution like this is exactly what interviewers look for.
