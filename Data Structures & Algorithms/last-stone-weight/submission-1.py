
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while(len(stones) > 1):
            heavy1 = heapq.heappop_max(stones)
            heavy2 = heapq.heappop_max(stones)
            if heavy1 == heavy2:
                continue
            else:
                heavy1 = heavy1 - heavy2
                heapq.heappush_max(stones, heavy1)
        if stones:
            return heapq.heappop(stones)
        
        return 0