#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/16
"""
from collections import Counter


# Given a string paragraph and a string array of the banned words banned,
# return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.split(" |!|\?|\'|\,|\;|\.", paragraph)
        c = {}
        for word in words:
            word = word.lower()
            c[word] = c.get(word, 0) + 1
        sorted_c = sorted(c.items(), key=lambda d:d[1], reverse=True)
        print(sorted_c)
        for num in sorted_c:
            if num.isalpha() and num[0] not in banned:
                print(num[0])
                return num[0]


if __name__ == "__main__":
    s = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    s.mostCommonWord(paragraph, banned)
