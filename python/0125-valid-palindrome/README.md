# 125.Valid Palindrome

## Problem Summary

You are given a string `s`.  

Your task is to determine whether `s` is a **valid palindrome**, considering **only alphanumeric characters** (letters and digits) and **ignoring cases**.

- Uppercase and lowercase letters should be treated the same.
- Any characters that are not letters or digits (spaces, commas, punctuation, etc.) should be ignored.

### Example 1

```text
Input:  s = "A man, a plan, a canal: Panama"
Output: true
Explanation: After removing non-alphanumeric characters and converting to lowercase, 
             we get "amanaplanacanalpanama", which is a palindrome.
```

### Example 2

```text
Input:  s = "race a car"
Output: false
Explanation: After filtering and lowercase, we get "raceacar", which is not a palindrome.
```

---

## Intuition

A **palindrome** is a string that reads the same forwards and backwards.

However, this problem is slightly tricky because:

- We must **ignore non-alphanumeric characters** (like spaces, commas, colons).
- We must **ignore case** (e.g., `A` and `a` are considered equal).

Instead of building a new filtered string and reversing it, we can:

- Use a **two-pointer technique**,  
- One pointer starting from the **left** of the string,  
- One pointer starting from the **right**,  
- Move them towards each other while:
  - **Skipping non-alphanumeric** characters,
  - Comparing lowercase characters for equality.

If all matched characters are equal until the pointers meet or cross, the string is a valid palindrome.

---

## Approach (Two Pointers with Alphanumeric Filtering)

The core idea of your code is:

1. Convert the string to **lowercase** at the beginning:
   - This ensures case-insensitive comparison.

2. Initialize two pointers:
   - `left = 0` (start of the string),
   - `right = len(s) - 1` (end of the string).

3. While `left < right`:
   - Move `left` to the right until it points to an **alphanumeric** character.
     - Use `s[left].isalnum()` to check this.
   - Move `right` to the left until it points to an **alphanumeric** character.
   - Now compare `s[left]` and `s[right]`:
     - If they are **different**, the string is **not a palindrome**.
     - If they are equal, move both pointers:
       - `left += 1`
       - `right -= 1`

4. If the loop finishes without finding a mismatch:
   - All corresponding characters match → the string **is a palindrome**.

This approach avoids building an extra filtered string and works in **O(n)** time.

---

## Code (LeetCode-Compatible Version Based on Your Logic)

Below is a version of your logic aligned with LeetCode’s expected function signature and return type `bool`.  
The algorithm itself is the **same** as what you implemented:

```python
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Returns True if s is a valid palindrome, considering only alphanumeric
        characters and ignoring case. Otherwise returns False.
        """

        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters at left and right
            if s[left] != s[right]:
                return False

            # Move both pointers towards the center
            left += 1
            right -= 1

        # If we never found a mismatch, it's a palindrome
        return True
```

> Note:  
> - The **logic** is exactly what you wrote.  
> - Only formal aspects are adapted:
>   - Added `self` parameter.
>   - Return type is `bool` (`True` / `False`), not strings like `"is a palindrome"`.  
>   - Removed the external `print` call since LeetCode handles testing.

---

## Step-by-Step Walkthrough (With Your Logic)

Let’s walk through your algorithm on this input:

```python
s = "A man, a plan, a canal: Panama"
```

### Step 1: Lowercase

```python
s = s.lower()
# s = "a man, a plan, a canal: panama"
```

### Step 2: Initialize Pointers

```python
left = 0                  # points to 'a'
right = len(s) - 1        # points to 'a' (last character)
```

### Iteration 1

- `left = 0`, `right = 29` (for this string length)
- `s[left] = 'a'`, `s[right] = 'a'`
- Both are alphanumeric, so no need to skip.

Comparison:

```python
s[left] == s[right]  # 'a' == 'a' → True
```

- No mismatch → continue.

Move pointers:

```python
left = 1
right = 28
```

---

### Iteration 2

- `s[left] = ' '` (space), `s[right] = 'm'`

First inner while for `left`:

```python
while left < right and not s[left].isalnum():
    left += 1
```

- `s[1] = ' '` → not alphanumeric → `left = 2`
- `s[2] = 'm'` → alphanumeric → stop inner loop.

Second inner while for `right` (here `s[right]` is already alnum, so it doesn’t move):

```python
s[left] = 'm'
s[right] = 'm'
```

Comparison:

```python
s[left] == s[right]  # 'm' == 'm' → True
```

Move pointers:

```python
left = 3
right = 27
```

---

### Iteration 3 (and beyond)

The same pattern repeats:

- Skip spaces, commas, and colon characters with `isalnum()` checks.
- Compare lowercase letters/digits at current `left` and `right`.
- If any pair mismatches → immediately return “not palindrome” (or `False` in the LeetCode version).
- Otherwise, keep moving inward.

Eventually:

- `left` and `right` cross,
- No mismatches were found,
- The string is declared **a palindrome**.

---

## Time and Space Complexity

### Time Complexity

- In the **worst case**, each character is visited at most a constant number of times:
  - `left` moves at most `n` steps,
  - `right` moves at most `n` steps.
- All operations inside the while loops are **O(1)**.

Therefore:

\[
\text{Time Complexity} = O(n)
\]

where `n` is the length of the string.

### Space Complexity

- We are modifying `s` in-place to lowercase (or we can think of it as reused),
- Only a few integer variables (`left`, `right`),
- No extra data structures like arrays or lists.

Thus:

\[
\text{Space Complexity} = O(1)
\]

(ignoring the input and the constant-radius local variables).

---

## Edge Cases

Your logic (and the LeetCode-compatible code) correctly handles several edge cases:

### 1. Empty String

```python
s = ""
```

- `len(s) = 0`
- `left = 0`, `right = -1`
- Main `while left < right` is never entered.
- Function returns “is a palindrome” (or `True` in the boolean version).
- By convention, an empty string is considered a palindrome.

---

### 2. String with Only Non-Alphanumeric Characters

```python
s = ".,,,!!!"
```

- After converting to lowercase (no change), pointers start at both ends.
- Inner loops move `left` and `right` inward until `left >= right`.
- No mismatch occurs; there are no alphanumeric characters to compare.
- Returns palindrome → consistent with the usual interpretation (no letters or digits → trivially symmetric).

---

### 3. Single Character

```python
s = "a"
```

- `left = 0`, `right = 0`.
- Main loop `while left < right` doesn’t run.
- Returns palindrome.

---

### 4. Mismatch Case

```python
s = "race a car"
```

After filtering (conceptually): `"raceacar"`.

- `r` vs `r` → OK
- `a` vs `a` → OK
- `c` vs `c` → OK
- `e` vs `a` → mismatch

At the point where `s[left] != s[right]`:

- Your code returns `"is not a palindrome"`.
- LeetCode version returns `False`.

---

## Key Takeaways

- This problem is a classic **two-pointer** interview question:
  - One pointer from the **left**, one from the **right**.
  - Move pointers inward while skipping irrelevant characters.
- Using `str.isalnum()` is a clean way to **filter** characters.
- Lowercasing at the beginning simplifies case-insensitive comparison.
- You achieve:
  - **O(n)** time,
  - **O(1)** extra space,
  which is optimal.
