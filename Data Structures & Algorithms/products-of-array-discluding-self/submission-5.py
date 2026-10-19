class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = nums[:]
        backward = nums[:]
        n = len(nums)
        for i in range(1, n):
            forward[i] = forward[i - 1] * forward[i]
            backward[n - 1 - i] = backward[n - i] * backward[n - 1 - i]
        res = backward[:]
        res[0] = backward[1]
        res[-1] = forward[-2]
        for i in range(1, n - 1):
            res[i] = forward[i - 1] * backward[i + 1]
        return res
        