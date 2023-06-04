class Solution(object):

    def __init__(self):
        self.visited = set()
        self.res = 0

    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        for e, m in enumerate(manager):
            if m == -1:
                continue
            graph[m].append(e)

        return self.dfs(headID, graph, informTime)

    def dfs(self, manager, graph, informTime):
        maxTime = 0
        for sub in graph[manager]:
            maxTime = max(maxTime, self.dfs(sub, graph, informTime))
        return maxTime + informTime[manager]



