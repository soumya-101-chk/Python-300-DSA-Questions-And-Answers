"""
278. Shopping Offers

Time Complexity: O(N * M) where N is offers, M is combinations
Space Complexity: O(M)
"""
from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dp = {}
        
        def dfs(curr_needs):
            if tuple(curr_needs) in dp:
                return dp[tuple(curr_needs)]
                
            res = sum(curr_needs[i] * price[i] for i in range(len(needs)))
            
            for offer in special:
                valid = True
                new_needs = []
                for i in range(len(needs)):
                    if curr_needs[i] < offer[i]:
                        valid = False
                        break
                    new_needs.append(curr_needs[i] - offer[i])
                    
                if valid:
                    res = min(res, offer[-1] + dfs(new_needs))
                    
            dp[tuple(curr_needs)] = res
            return res
            
        return dfs(needs)
