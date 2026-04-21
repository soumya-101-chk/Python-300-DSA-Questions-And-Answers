<div align="center">

<br/>

```
 █████╗ ██╗      ██████╗  ██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██║     ██╔════╝ ██╔═══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
███████║██║     ██║  ███╗██║   ██║█████╗  ██║   ██║██████╔╝██║  ███╗█████╗
██╔══██║██║     ██║   ██║██║   ██║██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝
██║  ██║███████╗╚██████╔╝╚██████╔╝██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
```

**Python · Data Structures & Algorithms · 300 Problems**

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Problems](https://img.shields.io/badge/Problems-300_Solved-22c55e?style=for-the-badge&logo=leetcode&logoColor=white)](.)
[![Complexity](https://img.shields.io/badge/Complexity-Annotated-8b5cf6?style=for-the-badge)](.)
[![License](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)](LICENSE)
[![PRs](https://img.shields.io/badge/PRs-Welcome-0ea5e9?style=for-the-badge)](CONTRIBUTING.md)

<br/>

> *"A junior should be able to read it. A senior should respect it."*

<br/>

</div>

---

## What is AlgoForge?

AlgoForge is the algorithmic core originally built for the **AlgoForge** platform — now open-sourced as a structured, opinionated reference for engineers preparing for senior-level technical interviews or sharpening competitive programming instincts.

Every solution was written with one rule: **no cryptic one-liners, no unexplained cleverness.** Just clean, well-documented, complexity-aware Python — the kind of code that gets written in real engineering environments.

<br/>

## Design Principles

```
┌─────────────────────────────┬────────────────────────────────────────────────┐
│ Principle                   │ What it means in practice                      │
├─────────────────────────────┼────────────────────────────────────────────────┤
│ Big-O Transparency          │ T: O(...) and S: O(...) declared on every file  │
│ Pythonic by Default         │ collections · heapq · bisect · itertools        │
│ Self-Documenting Names      │ complement, left_ptr — never x, tmp, arr2      │
│ Consistent Structure        │ class Solution: wraps every solution            │
└─────────────────────────────┴────────────────────────────────────────────────┘
```

<br/>

## Repository Layout

```
AlgoForge-Python-Core/
│
├── 1_Arrays_and_Hashing/           ── 40 problems  ─  Prefix sums, sliding windows
├── 2_Linked_Lists/                 ── 25 problems  ─  Fast/slow pointers, reversal
├── 3_Stacks_and_Queues/            ── 20 problems  ─  Monotonic stacks, deques
├── 4_Binary_Search/                ── 25 problems  ─  Search space, optimization
├── 5_Trees/                        ── 45 problems  ─  BST, Tries, DFS/BFS
├── 6_Recursion_and_Backtracking/   ── 25 problems  ─  Decision trees, pruning
├── 7_Graphs/                       ── 40 problems  ─  Dijkstra, Union-Find, Topo
├── 8_Heaps_and_Priority_Queues/    ── 15 problems  ─  K-way merges, two-heap
├── 9_Dynamic_Programming/          ── 50 problems  ─  Memoization, 1D/2D tables
└── 10_Greedy_and_Bit_Manipulation/ ── 15 problems  ─  Local optima, XOR tricks
```

> Problems are ordered by **pattern complexity** — following the repo top-to-bottom is a full curriculum, not a random walk.

<br/>

## Code Standard

Every solution follows this exact format. No exceptions.

```python
"""
╔══════════════════════════════════════════════════════════╗
║  Problem   :  Two Sum  (#1)                              ║
║  Difficulty:  Easy                                       ║
║  Pattern   :  Hash Map / Complement Lookup               ║
╠══════════════════════════════════════════════════════════╣
║  Time      :  O(N)                                       ║
║  Space     :  O(N)                                       ║
╠══════════════════════════════════════════════════════════╣
║  Approach  :  For each element, check whether its        ║
║  complement (target - num) was seen before.              ║
║  Store each index as we go — single pass, no sorting.    ║
╚══════════════════════════════════════════════════════════╝
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}  # value → index

        for current_idx, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], current_idx]

            seen[num] = current_idx

        return []  # Guaranteed solution exists per problem constraints
```

**What separates this from a raw LeetCode submission:**

- The docstring explains *why*, not just *what*
- Type hints on local variables where intent is ambiguous
- Inline comment on `seen` clarifies its semantic role at a glance
- `return []` annotated to show constraint awareness — signals deep problem understanding

<br/>

## Stats at a Glance

```
  300 problems  ·  10 categories  ·  100% complexity-annotated  ·  0 external dependencies
```

<br/>

## Getting Started

```bash
# 1. Clone
git clone https://github.com/soumya-101-chk/Python-300-DSA-Questions-And-Answers.git
cd Python-300-DSA-Questions-And-Answers

# 2. Isolated environment (recommended)
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Run any solution directly
python3 1_Arrays_and_Hashing/two_sum.py
```

No pip installs required. The standard library is all you need.

<br/>

## Contributing

This is a curated repo — quality over quantity. PRs are reviewed for:

| Type | Accepted if... |
|---|---|
| Bug fixes | Breaks a real edge case with proof |
| Complexity improvements | Genuinely better asymptotic bound |
| Test suites | Full `pytest` coverage for a module |

**Before opening a PR:**
1. Fork → create a semantic branch (`fix/two-sum-negative-nums`, `feat/dijkstra-tests`)
2. Confirm docstring complexity annotations are accurate
3. Match the code style above exactly — same docstring format, same structure
4. Write a one-paragraph PR description explaining the *why*

> Submissions that "also work" without improving clarity or complexity will be respectfully declined.

<br/>

## Roadmap

- [ ] `pytest` suite for all 300 problems
- [ ] `PATTERNS.md` — master cheat sheet of every pattern with examples
- [ ] LeetCode problem links embedded in every docstring
- [ ] Complexity curve visualizations per module

<br/>

---

<div align="center">

Built with rigor. Maintained with intent.

**[⭐ Star this repo](https://github.com/soumya-101-chk/Python-300-DSA-Questions-And-Answers)** if it levelled you up.

<br/>

`arrays` · `linked lists` · `trees` · `graphs` · `dynamic programming` · `greedy` · `backtracking`

</div>
