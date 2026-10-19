class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        nums.sort()
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            val = nums[i]
            p1 = i + 1
            p2 = length - 1
            while p1 < p2:
                val1 = nums[p1]
                val2 = nums[p2]
                if val + val1 + val2 == 0:
                    res.append([val, val1, val2])
                    while p1 < length and nums[p1] == val1:
                        p1 += 1
                    while p2 > 0 and nums[p2] ==  val2:
                        p2 -= 1
                elif val + val1 + val2 < 0:
                    p1 += 1
                else:
                    p2 -= 1
        return res