class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                del seen[num]
            else:
                seen[num] = num
        for key in seen:
            return key