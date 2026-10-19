class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        smallest = float('inf')
        for price in prices:
            res = max(res, price - smallest)
            smallest = min(price, smallest)
        return res