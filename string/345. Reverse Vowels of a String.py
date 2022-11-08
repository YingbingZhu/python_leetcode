#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/4
"""
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# Input: s = "leetcode"
# Output: "leotcede"


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                l += 1
                r -= 1
        return ''.join(s)


if __name__ == "__main__":
    s = Solution()
    s.reverseVowels("leetcode")