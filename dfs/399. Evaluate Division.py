import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #  build the graph
        graph = collections.defaultdict(dict)
        m = len(equations)
        for i in range(m):
            e = equations[i]
            graph[e[0]][e[1]] = values[i]
            graph[e[1]][e[0]] = 1.0 / values[i]
        print(graph)

        # DFS
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0
            
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][i] * temp
            return -1.0



        res = []
        for q in queries:
            res.append(dfs(q[0], q[1], set()))
        return res