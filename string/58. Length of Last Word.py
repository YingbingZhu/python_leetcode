#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/28
"""
# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = s.split(" ")
        for num in ls[::-1]:
            if num != '':
                return len(num)
        return 0




if __name__ == "__main__":
    s = Solution()
    s.lengthOfLastWord(s = "   fly me   to   the moon  ")