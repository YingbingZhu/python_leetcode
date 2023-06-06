class Solution(object):

    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        self.graph = self.construct_graph(bombs).graph
        # self.graph is a class
        res = 1
        for i in range(len(bombs)):
            visited = set()
            self.dfs(i, visited)
            res = max(res, len(visited))
        return res

    def dfs(self, e, visited):
        visited.add(e)
        for neigh in self.graph[e]:
            if neigh not in visited:
                self.dfs(neigh, visited)

    def construct_graph(self, bombs):
        graph = Graph()
        for i_source, source in enumerate(bombs):
            for i_dest, dest in enumerate(bombs):
                if i_source == i_dest:
                    continue
                if self.is_on_range(source, dest):
                    graph.add_edge(i_source, i_dest)
        return graph

    def is_on_range(self, a, b):
        """
        a and b are points
        """
        return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) <= a[2]


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, s, d):
        self.graph[s].append(d)