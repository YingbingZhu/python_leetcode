#!/usr/bin/env python
"""
 Created by ZhuYB at 2023/1/9
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur.left)
                stack.append(cur.right)
                res.append(cur.val)
        return res[::-1]

