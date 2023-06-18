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
        s = min(p.val, q.val)
        l = max(p.val, q.val)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val < s and node.right:
                stack.append(node.right)
            if node.val > l and node.left:
                stack.append(node.left)
        return node