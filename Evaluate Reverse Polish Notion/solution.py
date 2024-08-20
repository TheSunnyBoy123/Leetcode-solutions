import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(eval(str(b) + token + str(a))))
            else:
                stack.append(token)
        return int(stack[0])