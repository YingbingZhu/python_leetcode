#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/14
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inOrder(node):
            nonlocal res
            nonlocal prev
            nonlocal maxCount
            nonlocal count
            if not node:
                return
            inOrder(node.left)
            if node.val == prev:
                count += 1
            else:
                count = 1
                prev = node.val
            if count > maxCount:
                res = [node.val]
                maxCount = count
            elif count == maxCount and node.val not in res:
                res.append(node.val)
            inOrder(node.right)

        maxCount = 0
        count = 0
        res = []
        prev = -1
        inOrder(root, count)
        return res