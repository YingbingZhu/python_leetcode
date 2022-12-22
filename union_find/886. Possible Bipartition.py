class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            self.parents[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parents[py] = px
        else:
            self.parents[py] = px
            self.rank[px] += 1


class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(n + 1)]
        for d in dislikes:
            adj[d[0]].append(d[1])
            adj[d[1]].append(d[0])

        dsu = UF(n + 1)
        for i in range(1, n + 1):
            for neighbor in adj[i]:
                if dsu.find(i) == dsu.find(neighbor):
                    return False
                dsu.union(adj[i][0], neighbor)
        return True