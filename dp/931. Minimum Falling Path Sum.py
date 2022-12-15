#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/13
"""
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = matrix
        for i in range(1, len(matrix)):
            dp[i][0] += min(dp[i-1][0], dp[i-1][1])
            dp[i][-1] += min(dp[i-1][-1], dp[i-1][-2])
            for j in range(1, len(matrix[0])-1):
                dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

        print(dp)
        return min(dp[-1])


if __name__ == "__main__":
    s = Solution()
    input = [[2,1,3],[6,5,4],[7,8,9]]
    s.minFallingPathSum(input)
