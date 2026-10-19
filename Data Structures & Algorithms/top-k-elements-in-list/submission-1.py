class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1

        values = sorted(seen, key=seen.get, reverse=True)
        res = []
        for i in range(k):
            res.append(values[i])
        return res