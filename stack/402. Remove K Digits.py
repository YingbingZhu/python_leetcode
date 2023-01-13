class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            if stack or n != '0':
                stack.append(n)
        if k:
            stack = stack[:-k]
        return ''.join(stack) or '0'