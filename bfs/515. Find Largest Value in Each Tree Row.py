#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/4
"""
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            largest = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                if node.val > largest:
                    largest = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(largest)
        return res
