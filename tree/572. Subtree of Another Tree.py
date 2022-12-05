#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/2
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        def isIdentical(p, q):
            if not p or not q:
                return not p and not q
            return p.val == q.val and isIdentical(p.left, q.left) and isIdentical(p.right, q.right)

        if not root or not subRoot:
            return not root and not subRoot
        if isIdentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

