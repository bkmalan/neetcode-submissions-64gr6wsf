class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyingPrice = prices[0]

        for price in prices:
            maxProfit = max(maxProfit, price - buyingPrice)        
            buyingPrice = min(buyingPrice, price)

        return maxProfit