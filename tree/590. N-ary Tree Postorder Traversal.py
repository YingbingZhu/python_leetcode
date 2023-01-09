#!/usr/bin/env python
"""
 Created by ZhuYB at 2023/1/9
"""
# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                for child in node.children:
                    stack.append(child)
                res.append(node.val)
        return res[::-1]
