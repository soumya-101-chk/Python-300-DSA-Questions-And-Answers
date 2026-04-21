"""
297. Sum of Two Integers

Time Complexity: O(1)
Space Complexity: O(1)
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in Python
        mask = 0xffffffff
        
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b) 
            b = carry
            
        # handles overflow
        return (a & mask) if b > 0 else a
