class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        starters = []
        for num in nums:
            if num - 1 not in seen:
                starters.append(num)
        res = 0
        for num in starters:
            curr = 0
            while(num in seen):
                num += 1
                curr += 1
                res = max(res, curr)
        return res