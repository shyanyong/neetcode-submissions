import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        sorted_by_value_asc = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        
        res = []
        all = list(sorted_by_value_asc.keys())

        for i in range(k):
            res.append(all[i])
        return res