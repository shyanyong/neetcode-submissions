class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        length = len(s)
        seen = set()
        res = 0
        
        while right < length:
            if left == right:
                seen.add(s[left])
                right += 1
                res = max(res, len(seen))
                continue
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            right += 1
            res = max(res, len(seen))
        
        return res