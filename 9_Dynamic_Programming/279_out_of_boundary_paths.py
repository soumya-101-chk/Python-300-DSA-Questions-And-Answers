"""
279. Out of Boundary Paths

Time Complexity: O(m * n * maxMove)
Space Complexity: O(m * n)
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        res = 0
        
        for _ in range(maxMove):
            temp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if r == m - 1: res = (res + dp[r][c]) % MOD
                    if c == n - 1: res = (res + dp[r][c]) % MOD
                    if r == 0: res = (res + dp[r][c]) % MOD
                    if c == 0: res = (res + dp[r][c]) % MOD
                    
                    temp[r][c] = (
                        (dp[r - 1][c] if r > 0 else 0) +
                        (dp[r + 1][c] if r < m - 1 else 0) +
                        (dp[r][c - 1] if c > 0 else 0) +
                        (dp[r][c + 1] if c < n - 1 else 0)
                    ) % MOD
            dp = temp
            
        return res
