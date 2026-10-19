class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for anag in strs:
            sorted_anag = ''.join(sorted(anag))
            anagrams[sorted_anag].append(anag)
        
        return list(anagrams.values())