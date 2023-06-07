class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        for i in range(31):
            # if the ith bit is 1
            if (c >> i) & 1:
                # 1 1: 1, 1 0: 0
                res += (((a>>i) & 1) == 0 and ((b>>i) & 1) == 0)
            # if the ith bit is 0
            else:
                res += (a>>i & 1)
                res += (b>>i & 1)
        return res
