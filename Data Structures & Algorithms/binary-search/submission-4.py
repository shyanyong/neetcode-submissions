class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = (right - left) // 2 + left
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            if nums[middle] > target:
                right = middle
        return -1