#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/8
"""
# Given a string s of lower and upper case English letters.
#
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
#
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them.
# You can keep doing this until the string becomes good.
#
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
#
# Notice that an empty string is also good.


class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            # upper and lower = 32
            if stack and abs(ord(ch) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == "__main__":
    s = Solution()
    s.makeGood("abBAcC")

