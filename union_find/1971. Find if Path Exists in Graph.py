#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/19
"""


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            if self.rank[parent_x] > self.rank[parent_y]:
                parent_x, parent_y = parent_y, parent_x
            # x is smaller group
            self.rank[parent_y] += self.rank[parent_x]
            self.parents[parent_x] = parent_y

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.find(source) == uf.find(destination)
