# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def get_avg(node, cnt, total_sum):
            if not node:
                return 0, 0
            left = get_avg(node.left, cnt, total_sum)
            right = get_avg(node.right, cnt, total_sum)
            cnt = 1 + left[0] + right[0]
            total_sum = node.val + left[1] + right[1]

            nonlocal ans
            ans += (node.val == total_sum // cnt)

            return cnt, total_sum

        get_avg(root, 0, 0)

        return ans
