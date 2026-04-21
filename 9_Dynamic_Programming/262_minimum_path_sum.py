"""
262. Minimum Path Sum

Time Complexity: O(M * N)
Space Complexity: O(1) modifying input
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    continue
                if r == 0:
                    grid[r][c] += grid[r][c - 1]
                elif c == 0:
                    grid[r][c] += grid[r - 1][c]
                else:
                    grid[r][c] += min(grid[r][c - 1], grid[r - 1][c])
                    
        return grid[ROWS - 1][COLS - 1]
