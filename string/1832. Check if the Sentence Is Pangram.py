#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/17
"""
# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters,
# return true if sentence is a pangram, or false otherwise.


class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        count = 0
        seen = set()
        for c in sentence:
            if c not in seen:
                seen.add(c)
                count += 1
        return len(seen) == 26


if __name__ == "__main__":
    s = Solution()
    s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")