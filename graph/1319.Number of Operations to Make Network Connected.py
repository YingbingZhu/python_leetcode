# There are n computers numbered 
# from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. 
# You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this 
# in order to make all the computers connected. If it is not possible, return -1.


from collections import defaultdict


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
            
        visited = set()
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for adj in graph[node]:
                dfs(adj)
            return 1
        
        
        #  number of DSUs - 1
        return sum(dfs(node) for node in range(n)) - 1
            
        


if __name__ == "__main__":
    s = Solution()
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    s.makeConnected(n, connections)