class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            length = len(string)
            res += '#'
            res += str(length)
            res += '#'
            res += string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        str_length = ''
        while s:
            s = s[1:]
            while s[0] != '#':
                str_length += s[0]
                s = s[1:]
            s = s[1:]
            res.append(s[:int(str_length)])
            s = s[int(str_length):]
            str_length = ''
        return res