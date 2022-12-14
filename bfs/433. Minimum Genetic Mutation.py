#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/2
"""


# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
#
# Suppose we need to investigate a mutation from a gene string start to a gene string end
# where one mutation is defined as one single character changed in the gene string.
#
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations.
# A gene must be in bank to make it a valid gene string.
#
# Given the two gene strings start and end and the gene bank bank,
# return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.
#
# Note that the starting point is assumed to be valid, so it might not be included in the bank.


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        q = deque([(0, start)])
        seen = set()
        seen.add(start)
        while q:
            steps, curr = q.popleft()
            if curr == end:
                return steps
            for i in range(len(curr)):
                for c in "ACGT":
                    next = curr[:i] + c + curr[i+1:]
                    if next not in seen and next in bank:
                        seen.add(next)
                        q.append((steps+1, next))
        return -1




