#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/14
"""
from collections import defaultdict


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)

        for i, v in enumerate(stones):
            for ii, vv in enumerate(stones):
                if ii == i:
                    continue
                if vv[0] == v[0] or vv[1] == v[1]:
                    graph[i].append(ii)

        visited = set()
        res = 0
        stack = [0]
        while stack:
            point = stack.pop()
            visited.add(point)
            for edge in graph[point]:
                if edge not in visited:
                    res += 1
                    visited.add(edge)
                    stack.append(edge)

        for i in range(len(stones)):
            if i not in visited:
                stack = [i]
                while stack:
                    point = stack.pop()
                    visited.add(point)
                    for edge in graph[point]:
                        if edge not in visited:
                            res += 1
                            visited.add(edge)
                            stack.append(edge)
        print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
    s.removeStones(stones)