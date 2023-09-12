"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:return node
        d = {}
        visited = set()
        q = deque([node])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr not in visited:
                    if curr not in d:
                        d[curr] = Node(curr.val)
                    for n in curr.neighbors:
                        if n not in d:
                            d[n] = Node(n.val)
                        d[curr].neighbors.append(d[n])
                        q.append(n)
                visited.add(curr)
        return d[node]
        