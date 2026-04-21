"""
267. Egg Dropping Puzzle

Time Complexity: O(N * K^2)
Space Complexity: O(N * K)
"""
class Solution:
    def eggDrop(self, n, k):
        dp = [[0 for x in range(k + 1)] for x in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i][1] = 1
            dp[i][0] = 0
            
        for j in range(1, k + 1):
            dp[1][j] = j
            
        for i in range(2, n + 1):
            for j in range(2, k + 1):
                dp[i][j] = float("inf")
                l, r = 1, j
                while l <= r:
                    mid = (l + r) // 2
                    broken = dp[i - 1][mid - 1]
                    survived = dp[i][j - mid]
                    res = 1 + max(broken, survived)
                    dp[i][j] = min(dp[i][j], res)
                    if broken > survived:
                        r = mid - 1
                    else:
                        l = mid + 1
                        
        return dp[n][k]
