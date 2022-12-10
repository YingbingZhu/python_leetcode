# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_depth = 1
        res = root.val

        def dfs(node, depth):
            nonlocal max_depth
            nonlocal res
            if not node:
                return
            if depth > max_depth:
                max_depth = depth
                res = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return res