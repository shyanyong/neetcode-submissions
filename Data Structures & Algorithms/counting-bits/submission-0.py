class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOne(n: int):
            res = 0
            while n:
                if n % 2 == 1:
                    res += 1
                n = n // 2
            return res
        res = []
        for i in range(n + 1):
            res.append(countOne(i))
        return res