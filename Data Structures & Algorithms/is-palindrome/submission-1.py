class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        palin = s[::-1]

        return palin == s