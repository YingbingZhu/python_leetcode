#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/15
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        print(dp)
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        print(dp)
        return dp[-1][-1]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    Solution().longestCommonSubsequence(text1, text2)