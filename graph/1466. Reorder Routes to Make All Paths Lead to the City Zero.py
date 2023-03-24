# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(-c[0])

        self.res = 0
        visited = set()
        def dfs(node):
            visited.add(abs(node))
            for child in graph[node]:
                if abs(child) not in visited:
                    if child > 0:
                        self.res += 1
                    dfs(abs(child))
        
        dfs(0)
        print(visited)
        print(graph)
        return self.res
 
 
 