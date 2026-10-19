class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('inf')
        max = 0
        for price in prices:
            if price < smallest:
                smallest = price
            curr = price - smallest
            if curr > max:
                max = curr
        
        return max