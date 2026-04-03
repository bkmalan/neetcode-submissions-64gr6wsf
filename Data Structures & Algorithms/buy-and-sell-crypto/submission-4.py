class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curPrice = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > curPrice:
                res = max(res, prices[i] - curPrice)
            curPrice = min(curPrice, prices[i])
        print(res)
        return res             

