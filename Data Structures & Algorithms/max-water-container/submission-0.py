class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        curr = 0
        while(l < r):
            height_l = heights[l]
            height_r = heights[r]
            min_height = min(height_l, height_r)
            curr = max(curr, min_height * (r- l))

            if min_height == height_l:
                l += 1
            else:
                r -= 1
        
        return curr