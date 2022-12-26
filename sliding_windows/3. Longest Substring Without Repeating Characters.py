#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/26
"""
# Given a string s, find the length of the longest
# substring
#  without repeating characters.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        seen = {}
        l = 0
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            max_length = max(max_length, r - l + 1)
            seen[s[r]] = r
        return max_length


if __name__ == '__main__':
    s = "pwwkew"
    Solution().lengthOfLongestSubstring(s)

