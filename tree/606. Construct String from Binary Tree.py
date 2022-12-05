#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/2
"""
# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree
# with the preorder traversal way, and return it.
#
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship
# between the string and the original binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        res = ''

        def dfs(node):
            nonlocal res
            if not node:
                return
            res += node.val
            if not node.left and not node.right:
                return
            res += '()'
            dfs(node.left)
            res += ')'
            if node.right:
                res += '('

        dfs(root)
        return res