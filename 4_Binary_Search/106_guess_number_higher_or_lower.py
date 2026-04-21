"""
106. Guess Number Higher or Lower

Time Complexity: O(log N)
Space Complexity: O(1)
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          0 if num is equal to the picked number
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        
        while True:
            m = (l + r) // 2
            res = guess(m) # Assuming guess API is provided
            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m\n