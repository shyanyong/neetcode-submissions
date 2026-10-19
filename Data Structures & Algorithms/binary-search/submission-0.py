class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0
        while left <= right:
            middle = left + (right - left) // 2
            midnum = nums[middle]
            if midnum == target:
                return middle
            if midnum < target:
                left = middle + 1
            if midnum > target:
                right = middle - 1
        
        return -1