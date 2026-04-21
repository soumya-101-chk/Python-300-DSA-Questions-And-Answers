"""
79. Removing Stars From a String

Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)\n