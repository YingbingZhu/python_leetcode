class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '/':
                d1 = stack.pop()
                d2 = stack.pop()
                stack.append(int(d2 / d1))
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '-':
                d1 = stack.pop()
                d2 = stack.pop()
                stack.append(d2 - d1)
            else:
                stack.append(int(t))
        return stack[-1]             
                

        