class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        forward = nums[:]
        backward = nums[:]
        for i in range(1, length):
            forward[i] = forward[i - 1] * forward[i]
            backward[length - i - 1] = backward[length - i - 1] * backward[length - i]
        res = [0] * length
        # a b c d
        # 1 2 4 6
        # a ab abc abcd
        # 1 2 8 48
        # abcd bcd cd d
        # 48 48 24 6
        # bcd acd abd abc
        # 48 24 12 8

        res[0] = backward[1]
        res[-1] = forward[-2]
        for i in range(1, length - 1):
            res[i] = forward[i  - 1] * backward[i + 1]
        return res