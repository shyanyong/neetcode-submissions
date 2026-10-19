class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        heightl = height[l]
        heightr = height[r]
        res = 0

        while(l < r):
            if heightl < heightr:
                l += 1
                heightl = max(heightl, height[l])
                res += heightl - height[l]
            else:
                r -= 1
                heightr = max(heightr, height[r])
                res += heightr - height[r]
            

        return res