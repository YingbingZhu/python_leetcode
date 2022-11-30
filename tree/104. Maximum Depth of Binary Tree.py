#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/30
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def getDepth(node):
            if not node:
                return 0
            left = getDepth(node.left)
            right = getDepth(node.right)
            return max(left, right) + 1

        res = getDepth(root)
        return res