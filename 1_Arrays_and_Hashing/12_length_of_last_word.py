"""
12. Length of Last Word

Time Complexity: O(N)
Space Complexity: O(1)
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
            
        return length
