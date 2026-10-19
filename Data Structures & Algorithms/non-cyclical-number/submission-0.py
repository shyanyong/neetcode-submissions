class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        def squares(i):
            num = i
            res = 0
            while(num > 0):
                res += (num % 10) ** 2
                num = num // 10
            return res
        val = squares(n)
        seen[n] = val
        while (val != 1):
            if val in seen:
                return False
            curr = squares(val)
            seen[val] = curr
            val = curr    
        return True