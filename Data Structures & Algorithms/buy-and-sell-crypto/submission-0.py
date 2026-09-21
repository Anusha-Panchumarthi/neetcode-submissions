class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minleft = prices[0] 
        res = 0
        for price in prices:
            res = max(res, price - minleft)
            minleft = min(price, minleft)

        return res