class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        profits = [0]
        for index, price in enumerate(prices):
            if price > minimum:
                profits.append(price - minimum)
            minimum = min(price, minimum)
        
        return max(profits)