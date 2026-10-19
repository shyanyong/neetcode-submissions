from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
                continue
            if c == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            if c == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
            if c == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
        
        return len(stack) == 0