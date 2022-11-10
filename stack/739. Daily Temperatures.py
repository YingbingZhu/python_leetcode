#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/9
"""
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n
        # store temp and index, monotonic decrease stack
        stack = []
        for i in range(n-1, -1, -1):
            temp = temperatures[i]
            # pop to get the closet larger one
            while stack and stack[-1][0] <= temp:
                stack.pop()
            # if not empty, then there is a one larger
            if stack:
                res[i] = stack[-1][1] - i
            stack.append([temp, i])
            print(stack)

        return res


if __name__ == "__main__":
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    s.dailyTemperatures(temperatures)
