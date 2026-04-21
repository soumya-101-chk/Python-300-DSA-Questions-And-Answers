"""
176. Path with Maximum Gold

Time Complexity: O(K * 4^K) where K is cells with gold
Space Complexity: O(K)
"""
from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
                
            temp = grid[r][c]
            grid[r][c] = 0
            
            res = temp + max(
                dfs(r + 1, c),
                dfs(r - 1, c),
                dfs(r, c + 1),
                dfs(r, c - 1)
            )
            
            grid[r][c] = temp
            return res
            
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    ans = max(ans, dfs(r, c))
                    
        return ans
