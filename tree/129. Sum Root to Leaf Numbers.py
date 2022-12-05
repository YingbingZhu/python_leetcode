#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/5
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        def dfs(node, path):
            nonlocal res
            if node:
                path = 10 * path + node.val
                if not node.left and not node.right:
                    res += path
                    return
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, 0)
        return res