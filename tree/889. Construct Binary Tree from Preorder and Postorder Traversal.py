#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/14
"""
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    preIndex = 0
    posIndex = 0
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1
        if root.val == postorder[postorder]:
            return
        root.left = self.constructFromPrePost(preorder, postorder)
        root.right = self.constructFromPrePost(preorder, postorder)
        self.posIndex += 1
        return root


