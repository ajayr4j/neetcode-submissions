class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        max_profit = 0
        for price in prices:
            if price > minimum:
                max_profit = max(price - minimum, max_profit)
            minimum = min(price, minimum)
        return max_profit