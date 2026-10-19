class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while True:
            value = numbers[p1] + numbers[p2]
            if value == target:
                return [p1 + 1, p2 + 1]
            if value < target:
                p1 += 1
            else:
                p2 -= 1