"""
37. Reverse Words in a String

Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # One-liner Pythonic way: return " ".join(s.split()[::-1])
        
        words = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                j = i
                while j < len(s) and s[j] != ' ':
                    j += 1
                words.append(s[i:j])
                i = j
            i += 1
            
        # Two pointer to reverse the list of words
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
            
        return " ".join(words)
