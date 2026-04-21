"""
171. Beautiful Arrangement

Time Complexity: O(K) where K is valid arrangements
Space Complexity: O(N)
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        visit = set()
        res = 0
        
        def backtrack(i):
            nonlocal res
            if i > n:
                res += 1
                return
            for num in range(1, n + 1):
                if num not in visit and (num % i == 0 or i % num == 0):
                    visit.add(num)
                    backtrack(i + 1)
                    visit.remove(num)
                    
        backtrack(1)
        return res
