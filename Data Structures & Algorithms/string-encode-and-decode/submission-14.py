class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            n = str(len(word))
            res += '#'
            res += n
            res += '#'
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        # print(s)
        n = len(s)
        curr = 0
        next_length = ""
        res = []
        while(curr < n):
            if s[curr] == '#':
                curr += 1
                while(s[curr] != '#'):
                    next_length += s[curr]
                    curr += 1
                curr += 1
            next = int(next_length)
            res.append(s[curr:curr+next])
            curr += next
            next_length = ""

        return res