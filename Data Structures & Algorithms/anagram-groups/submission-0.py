class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            sort = "".join(sorted(word))
            words[sort].append(word)
        res = []
        for values in words:
            res.append(words[values])
        return res