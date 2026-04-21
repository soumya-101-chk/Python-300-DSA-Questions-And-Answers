"""
272. Knight Probability in Chessboard

Time Complexity: O(K * N^2)
Space Complexity: O(N^2)
"""
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1.0
        moves = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
        
        for step in range(k):
            dp2 = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in moves:
                            if 0 <= r + dr < n and 0 <= c + dc < n:
                                dp2[r + dr][c + dc] += dp[r][c] / 8.0
            dp = dp2
            
        return sum(sum(row) for row in dp)
