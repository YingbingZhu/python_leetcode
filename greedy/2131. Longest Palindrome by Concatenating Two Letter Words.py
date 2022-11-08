#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/3
"""
# You are given an array of strings words. Each element of words consists of two lowercase English letters.
#
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order.
# Each element can be selected at most once.
#
# Return the length of the longest palindrome that you can create.
# If it is impossible to create any palindrome, return 0.
#
# A palindrome is a string that reads the same forward and backward.


# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
from collections import Counter


class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        counter = Counter(words)
        print(counter)
        for k, v in counter.items():
            p = k[::-1]
            if p == k and v > 1:
                res += (v // 2) * 4
                counter[k] -= (v // 2) * 2
                print(res)
                print(counter)
            elif p != k and counter[k] > 0 and counter[p] > 0:
                total = min(counter[p], v)
                print(total)
                res += total * 4
                counter[k] -= total
                counter[p] -= total
                print(counter)
        print(res)
        add = False
        for k, v in counter.items():
            if v > 0 and not add and k == k[::-1]:
                res += 2
                add = True
        print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    input = ["bb","bb"]
    s.longestPalindrome(input)

