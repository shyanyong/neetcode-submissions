class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            value = token
            if token == '+':
                value = int(stack.pop()) + int(stack.pop())
            if token == '*':
                value = int(stack.pop()) * int(stack.pop())
            if token == '/':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                value = int(val2 / val1)
            if token == '-':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                value = val2 - val1
            stack.append(int(value))
        return stack.pop()