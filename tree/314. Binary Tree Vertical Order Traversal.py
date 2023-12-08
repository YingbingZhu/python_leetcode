# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root:
        return []
      m = defaultdict(list)
      queue = [(root, 0)]
      queue = deque(queue)
      while queue:
        for i in range(len(queue)):
          cur, col = queue.popleft()
          m[col].append(cur.val)
          if cur.left:
            queue.append((cur.left, col-1))
          if cur.right:
            queue.append((cur.right, col+1))
      print(m)
      return dict(sorted(m.items())).values()
          