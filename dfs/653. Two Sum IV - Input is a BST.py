#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/9
"""
# Given the root of a Binary Search Tree and a target number k,
# return true if there exist two elements in the BST such that their sum is equal to the given target.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack = [root]
        path = set()
        while stack:
            node = stack.pop()
            if k - node.val in path:
                return True
            path.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False