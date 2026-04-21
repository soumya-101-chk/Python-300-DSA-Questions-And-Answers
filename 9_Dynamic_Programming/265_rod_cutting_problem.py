"""
265. Rod Cutting Problem

Time Complexity: O(N^2)
Space Complexity: O(N)
"""
class Solution:
    def cutRod(self, price, n):
        dp = [0 for x in range(n + 1)]
        
        for i in range(1, n + 1):
            max_val = float("-inf")
            for j in range(i):
                max_val = max(max_val, price[j] + dp[i - j - 1])
            dp[i] = max_val
            
        return dp[n]
