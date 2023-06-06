class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        res = 0
        if not isConnected:
            return res
        seen = set()
        n = len(isConnected)

        def dfs(r):
            for j, connected in enumerate(isConnected[r]):
                if j not in seen and connected == 1:
                    seen.add(j)
                    dfs(j)

        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
        return res


