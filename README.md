# LeetCode Solutions in Python

This repository contains my structured, long-term practice for LeetCode problems, implemented in Python 3.

For each problem, I aim to provide:

- ✅ Clean and readable code
- ✅ Clear explanation of the intuition and approach
- ✅ Time and space complexity analysis
- ✅ Notes on edge cases and possible variations

I solve problems on a **daily basis**, and update this repository and its documentation on a **weekly** schedule.

---

## Repository Structure

```text
leetcode-solutions/
├── README.md                     # Repository overview (this file)
├── python/
│   ├── 0001-two-sum/
│   │   ├── solution.py           # Final submitted solution
│   │   └── README.md             # Explanation, intuition, complexity
│   ├── 0121-best-time-to-buy-and-sell-stock/
│   │   ├── solution.py
│   │   └── README.md
│   ├── 0345-reverse-vowels-of-a-string/
│   │   ├── solution.py
│   │   └── README.md
│   └── ...                       # More problems, same structure
└── templates/
    └── problem-notes-template.md # Reusable template for per-problem notes
```

### Per-Problem Folder Convention

Each problem lives in its own directory:

```text
python/<id>-<kebab-case-problem-title>/
```

For example:

- `python/0026-remove-duplicates-from-sorted-array/`
- `python/0125-valid-palindrome/`
- `python/0344-reverse-string/`

Each problem directory contains:

- `solution.py`  
  → The final Python implementation submitted to LeetCode.

- `README.md`  
  → Problem summary, intuition, detailed step-by-step approach, time & space complexity, edge cases, and (optionally) alternative solutions.

---

## How to Navigate This Repository

You can explore the solutions in multiple ways:

1. **By Problem ID**

   If you know the LeetCode problem ID, jump directly to the corresponding folder under `python/`, for example:

   - [`python/0026-remove-duplicates-from-sorted-array/`](./python/0026-remove-duplicates-from-sorted-array/)
   - [`python/0125-valid-palindrome/`](./python/0125-valid-palindrome/)
   - [`python/0344-reverse-string/`](./python/0344-reverse-string/)

2. **By Difficulty / Topic**

   Use the tables below to browse problems by difficulty and tags  
   (two pointers, arrays, DP, graphs, etc.).  
   I update these tables weekly as I add new problems.

---

## Problem List

Note: These tables are maintained manually and updated regularly as I solve new problems.

### • Easy: 11

| ID   | Title  | Folder | Tags | Week | Day |
| ---- | ----- | ----- | ----- | ----- |----- |
| 0026 | Remove Duplicates from Sorted Array | [`python/0026-remove-duplicates-from-sorted-array/`](./python/0026-remove-duplicates-from-sorted-array/) | Array, Two Pointers | 01 | 01 |
| 0027 | Remove Element   | [`python/0027-remove-element/`](./python/0027-remove-element/) | Array, Two Pointers | 01 | 01 |
| 0283 | Move Zeroes   | [`python/0283-move-zeroes/`](./python/0283-move-zeroes/) | Array, Two Pointers | 01 | 02 |
| 0088 | Merge Sorted Array   | [`python/0088-merge-sorted-array/`](./python/0088-merge-sorted-array/) | Array, Two Pointers, Sorting | 01 | 02 |
| 0977 | Squares of a Sorted Array  | [`python/0977-squares-of-a-sorted-array/`](./python/0977-squares-of-a-sorted-array/) | Array, Two Pointers, Sorting | 01 | 03 |
| 0344 | Reverse String  | [`python/0344-reverse-string/`](./python/0344-reverse-string/) | Two Pointers, String | 01 | 03 |
| 0345 | Reverse Vowels of a String  | [`python/0345-reverse-vowels-of-a-string/`](./python/0345-reverse-vowels-of-a-string/) | Two Pointers, String | 01 | 04 |
| 0125 | Valid Palindrome | [`python/0125-valid-palindrome/`](./python/0125-valid-palindrome/) | Two Pointers, String | 01 | 04 |
| 0680 | Valid Palindrome II | [`python/0680-valid-palindrome-II/`](./python/0680-valid-palindrome-II/) | Two Pointers, String, Greedy | 01 | 06 |
| 0643 | Maximum Average Subarray I | `python/0643-maximum-average-subarray-I/` | Array, Sliding Window | 02 | 08 |
| 0219 | Contains Duplicate II | `python/0219-contains-duplicate-II/` | Array, Hash Table, Sliding Window | 02 |10 |

### • Medium: 07 

| ID   | Title  | Folder | Tags | Week | Day |
| ---- | ----- | ----- | ----- | ----- |----- |
| 0167 | Two Sum II - Input Array Is Sorted   | [`python/0167-two-sum-II-input-array-is-sorted/`](./python/0167-two-sum-II-input-array-is-sorted/) | Array, Two Pointers, Binary Search |01 | 07 |
| 1343 | Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold | `python/1343-number-of-sub-arrays-of-size-K-and-average-greater-than-or-equal-to-threshold/` | Array, Sliding Window | 02 | 08 |
| 1456 | Maximum Number of Vowels in a Substring of Given Length | `python/1456-maximum-number-of-vowels-in-a-substring-of-given-length/` | String, Sliding Window | 02 |09 |
| 1052 | Grumpy Bookstore Owner  | `python/1052-grumpy-bookstore-owner/` | Array, Sliding Window | 02 |09 |
| 0209 | Minimum Size Subarray Sum | `python/0209-minimum-size-subarray-sum/` | Array, Sliding Window, Binary Search, Prefix Sum | 02 | 10 |
| 0003 | Longest Substring Without Repeating Characters | `python/0003-longest-substring-without-repeating-characters/` | Hash Table, String, Sliding Window | 02 | 11 |
| 0438 | Find All Anagrams in a String | `python/0438-find-all-anagrams-in-a-string/` | Hash Table, String, Sliding Window | 02 | 11 |


### • Hard: 0

| ID   | Title  | Folder | Tags | Week | Day |
| ---- | ----- | ----- | ----- | ----- |----- |
| ---- | ----- | ----- | ----- | ----- |----- |

> As I progress, I will replace the placeholder rows with actual problems and add more tags (e.g., `array`, `two-pointers`, `sliding-window`, `dp`, `graph`).

---

## Topics Coverage

This repository is part of a structured plan to cover a broad range of algorithmic topics, including (but not limited to):

- **Arrays & Hashing**
- **Two Pointers**
- **Sliding Window**
- **Binary Search**
- **Linked Lists**
- **Trees & Binary Search Trees**
- **Recursion & Backtracking**
- **Dynamic Programming**
- **Graphs** (BFS, DFS, shortest paths, topological sort, etc.)
- **Greedy Algorithms**
- **Heaps & Priority Queues**
- **Strings & Parsing**

Over time, I may add:

- Per-topic indexes (e.g., `topics/two-pointers.md`)
- Cross-links between related problems that share similar patterns

---

## Workflow & Goals

### Practice Workflow

- **Daily**: Solve one or more LeetCode problems (primarily in Python)
- **Per Problem**:
  - Implement and submit the solution on LeetCode
  - Save the final solution as `solution.py`
  - Write or update `README.md` in the problem’s folder using the shared template
- **Weekly**:
  - Update the main `README.md` problem tables (by difficulty and tags)
  - Refactor / improve explanations as needed

### Goals

- Build strong **problem-solving** and **algorithmic thinking**
- Prepare for **technical coding interviews**
- Maintain a clean, well-structured reference of:
  - Common patterns (two pointers, sliding window, DP, etc.)
  - Typical interview-style problems and their solutions
- Share clear explanations that may be helpful to others learning the same material

---

## Templates

The `templates/` directory contains:

- `problem-notes-template.md`  
  A reusable Markdown template for per-problem documentation, including sections such as:

  - Problem Summary
  - Intuition
  - Approach (step-by-step reasoning)
  - Complexity Analysis (Time & Space)
  - Edge Cases
  - Implementation (Python)
  - Improvements / Variations

This keeps documentation consistent across all problems.

---

## Notes

- All solutions are written in **Python 3**.
- Many problems have more than one valid approach  
  (e.g., brute force vs. optimized, different data structures, different patterns).
- When it is instructive, I aim to document:
  - A straightforward / brute-force solution
  - And then an optimized solution with a clear explanation of *why* it’s better.

---

## License

Unless stated otherwise, all code and documentation in this repository are provided under the MIT License.

You are free to read, use, and adapt the code, but please keep the license and attribution.

See [`LICENSE`](./LICENSE) for details.


