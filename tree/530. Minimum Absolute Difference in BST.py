#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/14
"""
# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.path = []

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inOrder(root)
        ans = float('inf')
        for i in range(len(self.path)-1):
            ans = min(ans, abs(self.path[i] - self.path[i+1]))
        return ans


    def inOrder(self, node):
        if not node:
            return
        if node.left:
            self.inOrder(node.left)
        self.path.append(node.val)
        if node.right:
            self.inOrder(node.right)
