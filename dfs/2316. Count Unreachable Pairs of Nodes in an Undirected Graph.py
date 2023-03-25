class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)
            size = 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    size += dfs(neighbor)
            return size
        

        ans = n * (n - 1) // 2
        components = []
        for i in range(n):
            if i not in visited:
                components.append(dfs(i))
        for k in components:
            ans -= k * (k - 1) // 2
        return ans