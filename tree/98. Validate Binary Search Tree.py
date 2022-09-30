#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/30
"""

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inOrder(root, output):
            if not root:
                return
            if root.left:
                inOrder(root.left, output)
            output.append(root.val)
            if root.right:
                inOrder(root.right, output)

        path = []
        inOrder(root, path)
        for i in range(1, len(path)):
            if path[i] <= path[i-1]:
                return False

        return True

