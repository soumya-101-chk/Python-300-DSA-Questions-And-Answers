"""
250. Best Time to Buy and Sell Stock with Cooldown

Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # state=(i, buying)
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
                
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
                
            return dp[(i, buying)]
            
        return dfs(0, True)
