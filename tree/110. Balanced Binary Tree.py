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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            if left == -1:
                return -1
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return False if check(root) == -1 else True