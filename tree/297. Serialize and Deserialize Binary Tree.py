#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/7
"""
from collections import deque


# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string
# and this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data[0] == '#':
            return None
        lst = data.split(",")
        root = TreeNode(int(lst[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if lst[index] != '#':
                node.left = TreeNode(int(lst[index]))
                queue.append(node.left)
            index += 1
            if lst[index] != '#':
                node.right = TreeNode(int(lst[index]))
                queue.append(node.right)
            index += 1
        return root




if __name__ == "__main__":
    ser = Codec()
    ser.serialize(root)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))