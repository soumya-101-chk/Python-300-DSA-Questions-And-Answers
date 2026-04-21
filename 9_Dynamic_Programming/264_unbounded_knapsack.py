"""
264. Unbounded Knapsack

Time Complexity: O(N * W)
Space Complexity: O(W)
"""
class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0 for i in range(W + 1)]
        
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if wt[i-1] <= w:
                    dp[w] = max(dp[w], dp[w-wt[i-1]] + val[i-1])
                    
        return dp[W]
