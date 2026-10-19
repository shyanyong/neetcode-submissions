class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in seen:
                curr = 0
                while(num in seen):
                    num += 1
                    curr += 1
                    res = max(res, curr)
        return res