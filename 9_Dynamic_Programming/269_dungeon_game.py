"""
269. Dungeon Game

Time Complexity: O(M * N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        dp = [float("inf")] * (COLS + 1)
        dp[COLS - 1] = 1
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                min_health = min(dp[c], dp[c + 1]) - dungeon[r][c]
                dp[c] = max(1, min_health)
                
        return dp[0]
