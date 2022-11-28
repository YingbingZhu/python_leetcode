#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/28
"""
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [[1] * i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                # numRows = 3, dp[2][1] = 1 + 1 = 2;
                # numRows = 4, dp[2][1] = 1 + 1 = 2;
                # dp[3][1] = dp[2][0] + dp[2][1] = 1 + 2 = 3;
                # dp[3][2] = dp[2][1] + dp[2][2] = 2 + 1 = 3;
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        print(dp)
        return dp


if __name__ == "__main__":
    s = Solution()
    s.generate(numRows=4)