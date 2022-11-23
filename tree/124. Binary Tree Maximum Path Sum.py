#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/23
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = float("-inf")

        def getMaxDepth(node):
            nonlocal res
            if not node:
                return 0
            left = max(0, getMaxDepth(node.left))
            right = max(0, getMaxDepth(node.right))
            res = max(res, left + right + node.val)
            return max(left, right) + node.val

        getMaxDepth(root)
        return res
