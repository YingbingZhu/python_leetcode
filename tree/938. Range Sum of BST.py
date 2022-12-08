#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/7
"""
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return
            dfs(node.left)
            if low <= node.val <= high:
                res += node.val
            dfs(node.right)

        dfs(root)
        return res

