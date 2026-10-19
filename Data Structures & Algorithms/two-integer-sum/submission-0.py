class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in remainder:
                return [remainder[val], i]
            remainder[target - val] = i
