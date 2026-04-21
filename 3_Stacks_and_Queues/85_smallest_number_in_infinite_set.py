"""
85. Smallest Number in Infinite Set

Time Complexity: popSmallest O(log N), addBack O(log N)
Space Complexity: O(N)
"""
import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1
        self.added = set()
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            res = heapq.heappop(self.heap)
            self.added.remove(res)
            return res
        res = self.cur
        self.cur += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.cur and num not in self.added:
            self.added.add(num)
            heapq.heappush(self.heap, num)\n