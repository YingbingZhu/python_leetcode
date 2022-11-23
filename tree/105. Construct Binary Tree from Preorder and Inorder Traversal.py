#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/23
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # store the index of value in inorder
        d = {}
        for i, v in enumerate(inorder):
            d[v] = i

        index = 0

        def arrayToTree(left, right):
            nonlocal index
            if left > right:
                return
            rootVal = preorder[index]
            root = TreeNode(rootVal)
            index += 1
            index1 = d[rootVal]
            root.left = arrayToTree(left, index1 - 1)
            root.right = arrayToTree(index1 + 1, right)


            return root

        return arrayToTree(0, len(preorder) - 1)




