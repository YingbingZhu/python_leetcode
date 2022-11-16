#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/16
"""
from collections import deque


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return [i for i in range(n)]
        neighbors = [set() for _ in range(n)]
        for i, j in edges:
            neighbors[i].add(j)
            neighbors[j].add(i)

        queue = deque()
        # initialize queue with leaf nodes
        for i, n in enumerate(neighbors):
            if len(n) == 1:
                queue.append(i)

        nodes = len(neighbors)
        while nodes > 2:
            curr = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                # removed nodes + 1
                curr += 1
                neighbor = neighbors[node].pop()
                neighbors[neighbor].remove(node)
                # after remove, add new leaf nodes
                if len(neighbors[neighbor]) == 1:
                    queue.append(neighbor)
            nodes -= curr

        return queue


if __name__ =="__main__":
    s = Solution()
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    s.findMinHeightTrees(n, edges)