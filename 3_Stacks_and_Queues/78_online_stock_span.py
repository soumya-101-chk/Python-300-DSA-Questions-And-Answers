"""
78. Online Stock Span

Time Complexity: O(1) amortized
Space Complexity: O(N)
"""
class StockSpanner:
    def __init__(self):
        self.stack = [] # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span\n