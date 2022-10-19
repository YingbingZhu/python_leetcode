#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/17
"""
# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with the same node values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        path_map = {}
        res = []

        def rec(node):
            if not node:
                return '#'
            path = ','.join([str(node.val), rec(node.left), rec(node.right)])

            path_map[path] = path_map.get(path, 0) + 1
            if path_map[path] == 2:
                res.append(node)

            return path

        rec(root)
        return res



