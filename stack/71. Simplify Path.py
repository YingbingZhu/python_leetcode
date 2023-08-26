class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split('/')
        print(lst)
        for t in lst:
            if stack and t == '..':
                stack.pop()
            elif t not in ('..', '', ' ', '.', '/'):
                stack.append(t)
        return '/' + '/'.join(stack)

