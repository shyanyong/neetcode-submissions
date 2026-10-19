class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def bsearch(l, r, target):
            while (l < r):
                mid = l + (r - l) // 2
                if numbers[mid] == target:
                    return mid
                if numbers[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return -1

        n = len(numbers)
        for i in range(n):
            val = bsearch(i, n, target - numbers[i])
            if val == -1:
                continue
            else:
                return [i + 1, val + 1]