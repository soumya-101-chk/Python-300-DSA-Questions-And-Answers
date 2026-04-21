"""
229. Rearrange String k Distance Apart

Time Complexity: O(N log A) where A is size of alphabet
Space Complexity: O(A)
"""
import collections
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s
        
        count = collections.Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        
        res = []
        q = collections.deque()
        
        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            res.append(char)
            q.append([cnt + 1, char])
            
            if len(q) >= k:
                nxtCnt, nxtChar = q.popleft()
                if nxtCnt < 0:
                    heapq.heappush(maxHeap, [nxtCnt, nxtChar])
                    
        return "".join(res) if len(res) == len(s) else ""
