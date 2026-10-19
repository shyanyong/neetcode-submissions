class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        curr = 0
        stack = []
        
        # if i see a larger number, i am remove from stack and add.
        # if not, i add to stack.
        # top of stack will always be the smallest
        # when i see a new temp, i will check my stack to see how many i can clear
        for i in range(length):
            if not stack:
                stack.append([temperatures[i], i])
                continue
            while stack:
                if stack[-1][0] >= temperatures[i]:
                    break
                else:
                    curr = stack.pop()
                    result[curr[1]] = i - curr[1]
            stack.append([temperatures[i], i])
        return result