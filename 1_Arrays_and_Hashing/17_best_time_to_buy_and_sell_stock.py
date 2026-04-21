"""
17. Best Time to Buy and Sell Stock

Time Complexity: O(N)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l=buy, r=sell
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
            
        return maxP
