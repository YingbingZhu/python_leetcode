#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/19
"""
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b
# where v = |a.val - b.val| and a is an ancestor of b.
#
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0


        def dfs(node, cur_max, cur_min):
            nonlocal res
            if not node:
                return
            res = max(res, abs(cur_max - node.val), abs(cur_min - node.val))
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            dfs(node.left, cur_max, cur_min)
            dfs(node.right, cur_max, cur_min)

        dfs(root, root.val, root.val)

        return res
