class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return min(cost)
        smallest = [float("inf")] * n
        smallest[0] = cost[0]
        smallest[1] = cost[1]

        for i in range(2, n):
            print(i)
            smallest[i] = min(smallest[i - 1], smallest[i - 2]) + cost[i]
            print(smallest[i])

        return min(smallest[n - 1], smallest[n - 2])
        # return smallest[n]
        # return 0