"""
271. Best Time to Buy and Sell Stock IV

Time Complexity: O(N * K)
Space Complexity: O(K)
"""
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
            
        if k >= len(prices) // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))
            
        cost = [float('inf')] * (k + 1)
        profit = [0] * (k + 1)
        
        for p in prices:
            for i in range(1, k + 1):
                cost[i] = min(cost[i], p - profit[i - 1])
                profit[i] = max(profit[i], p - cost[i])
                
        return profit[k]
