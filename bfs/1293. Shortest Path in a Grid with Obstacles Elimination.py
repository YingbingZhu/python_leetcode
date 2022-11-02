from collections import deque
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        if k > len(grid) - 1 + len(grid[0]) - 1:
            return len(grid) - 1 + len(grid[0]) - 1
        while queue:
            r, c, e, steps = queue.popleft()
            for rr, cc in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]:
                if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                    if grid[rr][cc] == 1 and e > 0 and (rr, cc, e-1) not in visited:
                        visited.add((rr, cc, e-1))
                        queue.append((rr, cc, e-1, steps+1))
                    if grid[rr][cc] == 0 and (rr, cc, e) not in visited:
                        if rr == len(grid)-1 and cc == len(grid[0])-1:
                            return steps + 1
                        visited.add((rr, cc, e))
                        queue.append((rr, cc, e, steps+1))
        return -1