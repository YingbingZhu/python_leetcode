#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/11
"""
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def isPalindrome(st):
            return st == st[::-1]

        def backtrack(path, index):
            if index == len(s):
                # copy path
                res.append(list(path))
                return
            for i in range(index, len(s)):
                if isPalindrome(s[index:i+1]):
                    path.append(s[index:i+1])
                    backtrack(path, i+1)
                    path.pop()
        backtrack([], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    s.partition("aab")

