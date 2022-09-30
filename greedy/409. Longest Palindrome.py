#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/30
"""
# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # counter occurrence of character
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        length = 0
        for k, v in counter.items():
            length += v // 2 * 2
            # current result is even and current value has one left
            if length % 2 == 0 and v % 2 == 1:
                length += 1

        return length


if __name__ == "__main__":
    nums = "abbbcc"
    s = Solution()
    print(s.longestPalindrome(nums))
