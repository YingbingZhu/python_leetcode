class UF:
    def __init__(self, n):
        self.parent = {}
        for i in range(1, n+1):
            self.parent[i] = i

    # Find the root of the set in which element `k` belongs
    def find(self, k):

        # if `k` is root
        if self.parent[k] == k:
            return k

        # recur for the parent until we find the root
        return self.find(self.parent[k])

    # Perform Union of two subsets
    def union(self, a, b):

        # find the root of the sets in which elements `x` and `y` belongs
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y


class Solution:
    def minScore(self, n, roads):
        d = [[] for _ in range(1, n+1)]

        # add edges to the undirected graph (add each edge once only to avoid
        # detecting cycles among the same edges, say x -> y and y -> x)
        for road in roads:
            src = road[0]
            dest = road[1]
            d[src].append(dest)

        uf = UF(n)
        for u in range(n):
            for v in d[u]:
                print(u, v)
                x = uf.find(u)
                y = uf.find(v)
                uf.union(x, y)


        print(uf.parent)
        print(d)


if __name__ == "__main__":
    s = Solution()
    n = 4
    roads = [[1, 2, 2], [1, 3, 4], [3, 4, 7]]
    s.minScore(n, roads)