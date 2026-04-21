# Python 300 DSA Questions & Answers Roadmap

A comprehensive, highly-curated repository containing 300 optimal Data Structures and Algorithms solutions in Python. Built to prepare for top-tier SWE technical interviews.

## 🚀 Overview

This repository provides clean, production-ready, and pedagogical solutions to 300 of the most fundamental and frequent algorithmic problems. Every solution includes explicitly documented **Time Complexity** and **Space Complexity**.

The roadmap is structured chronologically, advancing from foundational patterns to complex graph and DP theories.

## 📁 Repository Structure

The curriculum is divided into 10 structured sections:

1. **Arrays & Hashing (40 Questions)**
2. **Linked Lists (25 Questions)**
3. **Stacks & Queues (20 Questions)**
4. **Binary Search (25 Questions)**
5. **Trees (Binary Tree, BST, Tries) (45 Questions)**
6. **Recursion & Backtracking (25 Questions)**
7. **Graphs (BFS, DFS, Dijkstra, Union-Find) (40 Questions)**
8. **Heaps / Priority Queues (15 Questions)**
9. **Dynamic Programming (50 Questions)**
10. **Greedy & Bit Manipulation (15 Questions)**

## 💻 Code Style & Standards

- **Optimal Algorithms:** Prioritizing minimal Time/Space complexities.
- **Pythonic Implementations:** Leveraging core built-ins like `collections.deque`, `heapq`, and sets efficiently.
- **Teacher-Style Naming:** Descriptive, non-cryptic variable names optimized for readability and learning.

## 🛠 Usage

This repository serves as an excellent reference for daily DSA practice. 

```python
# Example: 1_Arrays_and_Hashing/1_two_sum.py

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
```
