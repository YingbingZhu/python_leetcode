#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/10
"""
# You are given a string s consisting of lowercase English letters.
# A duplicate removal consists of choosing two adjacent and equal letters and removing them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made.
# It can be proven that the answer is unique.


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            if res and res[-1] == c:
                res.pop()
                print(i)
            else:
                res += c
            i += 1
        print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates("azxxzy")
