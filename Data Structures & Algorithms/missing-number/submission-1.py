class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        largest = 0
        for num in nums:
            res += num
            largest += 1
        
        print(largest)
        val = largest * (largest + 1) // 2
        return val - res