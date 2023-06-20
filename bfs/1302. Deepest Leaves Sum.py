# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# take care of sum of each rows, each row will reset res = 0
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        q = deque([root])
        while q:
            res = 0
            for i in range(len(q)):
                node = q.popleft()
                res += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res