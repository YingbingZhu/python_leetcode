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
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return [0, 0]
            l = dfs(node.left)
            r = dfs(node.right)
            rob = node.val + l[1] + r[1]
            not_rob = max(l) + max(r)
            return [rob, not_rob]

        return max(dfs(root))

