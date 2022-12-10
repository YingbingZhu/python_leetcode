# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = float('-inf')

        def getSum(node):
            if not node:
                return 0
            return node.val + getSum(node.left) + getSum(node.right)

        totalSum = getSum(root)

        def dfs(node):
            nonlocal res
            nonlocal totalSum
            if not node:
                return 0
            current = node.val + dfs(node.left) + dfs(node.right)
            res = max(res, current * (totalSum - current))
            return current

        dfs(root)
        return res % (10 ** 9 + 7)
