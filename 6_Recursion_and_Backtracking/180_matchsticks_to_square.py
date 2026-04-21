"""
180. Matchsticks to Square

Time Complexity: O(4^N)
Space Complexity: O(N)
"""
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        if sum(matchsticks) % 4:
            return False
            
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
                
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                    
                    if sides[j] == 0:
                        break
                        
            return False
            
        return backtrack(0)
