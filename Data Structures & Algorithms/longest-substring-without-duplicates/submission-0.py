class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        seen = {}
        longest = 0
        curr = 0
        while(r < n):
            if s[r] in seen:
                seen.pop(s[l])
                l += 1
                curr -= 1
            else:
                seen[s[r]] = r
                r += 1
                curr += 1
                longest = max(longest, curr)
        return longest