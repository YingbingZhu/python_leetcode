# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# https://leetcode.com/problems/clone-graph/
from collections import deque


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node
        m = {}
        visited = set()
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            if curr not in m:
                m[curr] = Node(curr.val)
            for n in curr.neighbors:
                if n not in m:
                    m[n] = Node(n.val)
                # append copied neighbors
                m[curr].neighbors.append(m[n])
                q.append(n)
        return m[node]
