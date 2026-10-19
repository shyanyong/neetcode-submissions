class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1
        
        for c in t:
            if c not in chars:
                return False
            chars[c] -= 1
            if chars[c] < 0:
                print(chars)
                return False
        return True