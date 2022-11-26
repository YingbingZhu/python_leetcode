class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        tokens = path.split('/')
        for token in tokens:
            if token == ".." and stack:
                stack.pop()
            elif token not in ('.', ' ', '', '..'):
                stack.append(token)
        return '/' + '/'.join(stack)
