#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/2
"""
# A transformation sequence from word beginWord to word endWord
# using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList,
# return the number of words in the shortest transformation sequence from beginWord to endWord,
# or 0 if no such sequence exists.


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        q = deque([(beginWord, 0)])
        while q:
            curr, steps = q.popleft()
            if curr == endWord:
                return steps + 1
            for i in range(len(curr)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next = curr[:i] + c + curr[i+1:]
                    if next != beginWord and next in wordList:
                        wordList.remove(next)
                        q.append((next, steps + 1))
        return 0

