class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)

        for char in s:
            seen[char] += 1
        
        for char in t:
            seen[char] -= 1
        return all(value == 0 for value in seen.values()) 
