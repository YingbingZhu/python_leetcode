#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/29
"""
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# https://leetcode.com/problems/course-schedule/


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # construct graph and indegree dictionary
        graph = defaultdict(list)

        ind = defaultdict()
        for i in range(numCourses):
            ind[i] = 0

        for i in prerequisites:
            pre = i[1]
            after = i[0]
            graph[pre].append(after)
            ind[after] = ind.get(after, 0) + 1

        q = deque()
        for k, v in ind.items():
            if v == 0:
                q.append(k)

        courses = 0
        while q:
            curr = q.popleft()
            courses += 1
            for neigh in graph[curr]:
                ind[neigh] -= 1
                if ind[neigh] == 0:
                    q.append(neigh)

        return courses == numCourses



