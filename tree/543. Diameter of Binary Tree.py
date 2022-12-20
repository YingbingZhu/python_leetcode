#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/30
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        def getDepth(node):
            nonlocal res
            if not node:
                return 0
            left = getDepth(node.left)
            right = getDepth(node.right)
            diameters = left + right
            res = max(res, diameters)
            return max(left, right) + 1

        getDepth(root)
        return res
