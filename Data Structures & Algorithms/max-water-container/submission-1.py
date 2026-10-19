class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        water = 0
        while p1 < p2:
            h1 = heights[p1]
            h2 = heights[p2]
            shorter = min(h1, h2)
            water = max(shorter * (p2 - p1), water)
            if h1 > h2:
                p2 -= 1
            else:
                p1 += 1
        return water