#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/29
"""
from collections import Counter


# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        d = Counter(text)
        d['l'] = d['l'] // 2
        d['o'] = d['o'] // 2


        print(d)
        return min(d['b'], d['a'], d['l'], d['o'], d['n'])



if __name__ == "__main__":
    s = Solution()
    text ="fgsdgballorewn"
    s.maxNumberOfBalloons(text)


