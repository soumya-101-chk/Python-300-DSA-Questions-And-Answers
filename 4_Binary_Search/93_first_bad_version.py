"""
93. First Bad Version

Time Complexity: O(log N)
Space Complexity: O(1)
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m): # Assuming isBadVersion exists
                r = m
            else:
                l = m + 1
                
        return l\n