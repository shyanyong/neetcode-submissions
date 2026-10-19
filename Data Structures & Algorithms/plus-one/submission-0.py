class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        curr = len(digits) - 1
        while remainder:
            if curr == -1:
                digits = [1] + digits
                return digits
            if digits[curr] == 9:
                digits[curr] = 0
                curr -= 1
            else:
                digits[curr] += 1
                remainder = 0
        return digits