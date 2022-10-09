#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/10/8
"""


# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parents = {root: None}
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parents.update({node.left: node})
            if node.right:
                stack.append(node.right)
                parents.update({node.right: node})

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents.get(p)

        while q not in ancestors:
            q = parents.get(q)

        return q
