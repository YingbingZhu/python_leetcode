#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/2
"""
from collections import deque


# Given the root of a binary tree,
# return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        path = [root]
        q = deque(path)
        while q:
            current = []
            for _ in range(len(q)):
                node = q.popleft()
                current.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(current)
        return res
