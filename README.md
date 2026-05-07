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

- `python/0001-two-sum/`
- `python/0121-best-time-to-buy-and-sell-stock/`
- `python/0345-reverse-vowels-of-a-string/`

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

   - [`python/0001-two-sum/`](./python/0001-two-sum/)
   - [`python/0121-best-time-to-buy-and-sell-stock/`](./python/0121-best-time-to-buy-and-sell-stock/)
   - [`python/0345-reverse-vowels-of-a-string/`](./python/0345-reverse-vowels-of-a-string/)

2. **By Difficulty / Topic**

   Use the tables below to browse problems by difficulty and tags  
   (two pointers, arrays, DP, graphs, etc.).  
   I update these tables weekly as I add new problems.

---

## Problem List

Note: These tables are maintained manually and updated regularly as I solve new problems.

### Easy

| ID   | Title                                   | Folder                                                          | Tags                          |
| ---- | --------------------------------------- | ---------------------------------------------------------------- | ----------------------------- |
| 26 | Remove Duplicates from Sorted Array | ---------------------------------------------------------------- | Array, Two Pointers |
| 27 | Remove Element   | ---------------------------------------------------------------- | Array, Two Pointers |
| 283 | Move Zeroes   | ---------------------------------------------------------------- | Array, Two Pointers |
| 88 | Merge Sorted Array   | ---------------------------------------------------------------- | Array, Two Pointers, Sorting |
| 977 | Squares of a Sorted Array  | ---------------------------------------------------------------- | Array, Two Pointers, Sorting |
| 344 | Reverse String  | ---------------------------------------------------------------- | Two Pointers, String |
| 345 | Reverse Vowels of a String  | ---------------------------------------------------------------- | Two Pointers, String |
| 125 | Valid Palindrome | ---------------------------------------------------------------- | Two Pointers, String |

### Medium

| ID   | Title                                   | Folder                                                          | Tags                          |
| ---- | --------------------------------------- | ---------------------------------------------------------------- | ----------------------------- |
| ---- | --------------------------------------- | ---------------------------------------------------------------- | ----------------------------- |

### Hard

| ID   | Title                                   | Folder                                                          | Tags                          |
| ---- | --------------------------------------- | ---------------------------------------------------------------- | ----------------------------- |
| ---- | --------------------------------------- | ---------------------------------------------------------------- | ----------------------------- |

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


