#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/6
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n not in Solution.memo:
            res = []
            for x in range(n):
                y = n - x - 1
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        res.append(node)
            Solution.memo[n] = res

        return Solution.memo[n]



