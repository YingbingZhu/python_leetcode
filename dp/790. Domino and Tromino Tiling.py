class Solution(object):
    def __init__(self):
        self.dp = {}

    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n, 0, 0) % (10**9 + 7)

    def helper(self, n, x, y):
        if x > n or y > n:
            return 0
        if x == n and y == n:
            return 1
        if (x, y) in self.dp:
            return self.dp[(x, y)]
        res = 0
        if x == y:
            res += self.helper(n, x + 1, y + 1)
            res += self.helper(n, x + 2, y + 1)
            res += self.helper(n, x + 1, y + 2)
            res += self.helper(n, x + 2, y + 2)
        elif (x - y) == 1:
            res += self.helper(n, x+1, y+2)
            res += self.helper(n, x, y + 2)
        else:
            res += self.helper(n, x+2, y+1)
            res += self.helper(n, x+2, y)
        self.dp[(x,y)] = res
        return res



