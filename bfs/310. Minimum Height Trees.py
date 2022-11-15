#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/15
"""
from collections import deque


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        neighbors = [set() for _ in range(n)]
        for i, j in edges:
            neighbors[i].add(j)
            neighbors[j].add(i)

        queue = deque()
        for i, n in enumerate(neighbors):
            if len(n) == 1:
                queue.append(i)
        print(queue)
        while len(neighbors) > 2:
            for _ in range(len(queue)):
                node = queue.popleft()
                print(node)
                for neighbor in neighbors[node]:
                    neighbors[neighbor].remove(node)
                    print(neighbor)
                    if len(neighbors[neighbor]) == 1:
                        queue.append(neighbor)

        return queue


if __name__ == "__main__":
    s = Solution()
    edges = [[1,0],[1,2],[1,3]]
    s.findMinHeightTrees(4, edges)