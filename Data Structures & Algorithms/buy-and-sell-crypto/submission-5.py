class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        curr = prices[0]
        for price in prices:
                maxProfit = max(maxProfit, price - curr)
                curr = min(price, curr)
        
        return maxProfit