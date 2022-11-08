#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/3
"""
# Given a string s, return the longest palindromic substring in s.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = (0, 1)
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[j] == s[i]:
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if res[1] - res[0] < j - i + 1:
                            res = (i, j + 1)
        return s[res[0]:res[1]]


if __name__ == "__main__":
    s = Solution()
    input = "abab"
    s.longestPalindrome(input)



