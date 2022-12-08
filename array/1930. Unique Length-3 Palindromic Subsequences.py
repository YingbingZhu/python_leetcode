#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/7
"""
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".


class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        # find the left-most and right-most index and then add length
        count = 0
        begin = {}
        end = {}
        for i in range(len(s)):
            if s[i] not in begin:
                begin[s[i]] = i
            end[s[i]] = i
        for c in set(s):
            if begin[c] == end[c] or begin[c] == end[c] - 1:
                continue
            else:
                count += len(set(s[begin[c]+1:end[c]]))
        return count






if __name__ == "__main__":
    s = Solution()
    s1 = "aabca"
    s.countPalindromicSubsequence(s1)