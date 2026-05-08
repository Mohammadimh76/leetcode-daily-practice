# 680. Valid Palindrome II

## 1. Problem Description

You are given a string `s`.

You need to determine whether it is possible to make `s` a **palindrome** by **deleting at most one character**.

- A palindrome reads the same forward and backward.
- You are allowed to **delete at most one** character.
- You cannot rearrange characters; you can only remove at most one.

### Examples

#### Example 1

```text
Input:  s = "aba"
Output: true
Explanation: The string is already a palindrome. No deletion is needed.
```

#### Example 2

```text
Input:  s = "abca"
Output: true
Explanation:
  Remove 'b' → "aca", which is a palindrome.
  Or remove 'c' → "aba", also a palindrome.
```

#### Example 3

```text
Input:  s = "abc"
Output: false
Explanation:
  You can delete only one character:
    "bc" → not palindrome
    "ac" → not palindrome
    "ab" → not palindrome
  So it is impossible to make it a palindrome with at most one deletion.
```

---

## 2. High-Level Intuition

This is a classic extension of the **two-pointer palindrome** problem.

For a normal palindrome check:

- We use two pointers:
  - `left` from the start
  - `right` from the end
- While `left < right`, we compare `s[left]` and `s[right]`.
  - If they are equal, move inward.
  - If they differ, it's **not** a palindrome.

In this problem, we are allowed to **delete at most one character**. This means:

- When we encounter the **first mismatch** between `s[left]` and `s[right]`,we have two choices:
  1. **Skip the left character** (delete `s[left]`), and check if the remaining substring is a palindrome.
  2. **Skip the right character** (delete `s[right]`), and check if the remaining substring is a palindrome.

If **either** of these two options leads to a palindrome, then the answer is `true`.
If neither works, the answer is `false`.

---

## 3. Your Original Code (Analysis)

You wrote:

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() 
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1 
                right -= 1
            elif s[left] != s[right]:
                return self.Solution.isPalindrome(s, left + 1, right) or self.Solution.isPalindrome(s, left, right -1)
      
        return True

    def isPalindrome(s: str, left: int, right: int) -> bool:
      
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

### Issues in the Original Code

1. **Calling `self.Solution.isPalindrome` is incorrect**

   - `self.Solution` does **not** exist.
   - You should simply call `self.isPalindrome(...)`.
2. **`isPalindrome` is defined like a standalone function, not as an instance method**

   ```python
   def isPalindrome(s: str, left: int, right: int) -> bool:
   ```

   In a class, instance methods must have `self` as the first parameter:

   ```python
   def isPalindrome(self, s: str, left: int, right: int) -> bool:
   ```
3. Minor point: Using `s = s.lower()` is fine here (the problem doesn’t require case-sensitivity), but LeetCode usually assumes case-sensitive checking unless otherwise stated. Still, logically this doesn’t break the algorithm, just changes behavior slightly.

Because of points 1 and 2, your code **will not run correctly** in LeetCode as-is.
According to your instruction, when the code has issues, I must **fix it** and explain based on the **corrected** version.

---

## 4. Corrected Version of Your Code

Here is a fixed, LeetCode-compatible, and logically equivalent version of your intent:

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Try skipping left character or right character
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

        return True

    def isPalindrome(self, s, left, right):
        """
        Helper function to check if s[left:right+1] is a palindrome.
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

What changed compared to your original code:

- `self.Solution.isPalindrome(...)` → `self.isPalindrome(...)`
- `def isPalindrome(s: str, left: int, right: int) -> bool:` → `def isPalindrome(self, s, left, right):`
- Slightly simplified `elif s[left] != s[right]:` into just `else:`, because we are already in the `while` and it’s the only other case.

The **core algorithm** and your main idea remain exactly the same.

---

## 5. Step-by-Step Explanation of the Algorithm

We’ll describe the logic based on the corrected code.

### 5.1 Main Method: `validPalindrome`

```python
s = s.lower()
left, right = 0, len(s) - 1
```

- Convert `s` to lowercase (optional but consistent).
- Initialize two pointers:
  - `left` at the start,
  - `right` at the end.

---

### 5.2 Scanning from Both Ends

```python
while left < right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
```

- While `left < right`:
  - If the characters match:
    - Move both pointers inward.
  - If they **don’t** match:
    - This is the **first mismatch**.
    - We now decide whether we can fix this by deleting **at most one** character.

At the first mismatch, we try two options:

1. **Skip the left character**:

   ```python
   self.isPalindrome(s, left + 1, right)
   ```

   This simulates deleting `s[left]`, and checking if the substring `s[left+1 : right+1]` is a palindrome.
2. **Skip the right character**:

   ```python
   self.isPalindrome(s, left, right - 1)
   ```

   This simulates deleting `s[right]`, and checking if the substring `s[left : right]` is a palindrome.

If **either** of those substrings is a palindrome, we can fix the string by deleting at most one character → return `True`.

If neither is a palindrome, then even with one deletion, we cannot make `s` a palindrome → return `False`.

If the loop finishes without hitting the `else` branch (i.e., no mismatch), then the original string is already a palindrome → return `True`.

---

### 5.3 Helper Method: `isPalindrome`

```python
def isPalindrome(self, s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

This helper checks whether `s[left:right+1]` is a palindrome.

- Again, classical **two-pointer** palindrome check.
- If any mismatch occurs, it returns `False`.
- If we finish the loop without mismatch, it returns `True`.

This function is used **only once** after the first mismatch, on at most two intervals:

- `s[left+1 : right+1]`
- `s[left : right]`

---

## 6. Example Walkthrough

### Example: `s = "abca"`

We expect `True`, because deleting `'b'` or `'c'` makes it a palindrome.

1. Initial:

   ```python
   s = "abca"
   left = 0    # 'a'
   right = 3   # 'a'
   ```
2. First iteration:

   - `s[left] = 'a'`, `s[right] = 'a'` → equal.
   - Move inward:

     ```python
     left = 1   # 'b'
     right = 2  # 'c'
     ```
3. Second iteration:

   - `s[1] = 'b'`, `s[2] = 'c'` → mismatch.
   - Now we try:

     ```python
     self.isPalindrome(s, left + 1, right)  # isPalindrome("abca", 2, 2)  => "c"
     self.isPalindrome(s, left, right - 1)  # isPalindrome("abca", 1, 1)  => "b"
     ```
   - `isPalindrome("abca", 2, 2)`:

     - Substring: `"c"` → single character → palindrome → returns `True`.
   - Since the first call already returns `True`, the whole method returns `True`.

This matches the expected output.

---

## 7. Time and Space Complexity

### Time Complexity

- The main `while` loop in `validPalindrome` runs at most `O(n)` steps, where `n = len(s)`.
- In the **worst case**, when we find a mismatch once, we call `isPalindrome` on a substring of length at most `n - 1`.
- The helper `isPalindrome` takes O(n) in the worst case.

Therefore, total time complexity is:

\[
O(n) + O(n) = O(n)
\]

This is optimal for this problem.

### Space Complexity

- We do not use any extra data structures (no extra arrays or lists).
- We only use a few integer variables and references → O(1) additional space.

So:

\[
\text{Space Complexity} = O(1)
\]

---

## 8. Edge Cases

1. **Empty string** `""`

   - `left = 0`, `right = -1` → `left < right` is false → returns `True`.
   - An empty string is considered a palindrome.
2. **Single-character string** `"a"`

   - Similarly, loop doesn’t run → returns `True`.
3. **Already palindrome** `"racecar"`

   - No mismatch found → returns `True` directly.
4. **Needs exactly one deletion** `"abca"`

   - First mismatch at `'b'` and `'c'`.
   - One of the two options (`skip left` or `skip right`) yields a palindrome.
5. **Cannot be fixed with one deletion** `"abc"`

   - Mismatch at `'a'` and `'c'`.
   - Check `"bc"` and `"ab"` → neither is palindrome → return `False`.

---

## 9. Key Takeaways

- This problem is a **direct extension** of the classic palindrome check.
- Technique:
  - Use **two pointers** from both ends.
  - On mismatch, try **one deletion** (skip left or skip right).
  - Use a helper to verify palindromic substrings.
- Complexity:
  - Time: **O(n)**
  - Space: **O(1)**
- Structurally:
  - Main logic in `validPalindrome`.
  - Clean, reusable helper `isPalindrome` for substring checks.
