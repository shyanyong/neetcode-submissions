class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        lowered = s.lower()
        while(left <= right):
            l = lowered[left]
            r = lowered[right]
            print(l, r)
            if not l.isalnum():
                left += 1
                continue
            if not r.isalnum():
                right -= 1
                continue
            if l != r:
                return False
            left += 1
            right -= 1
        return True