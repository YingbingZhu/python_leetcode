class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        seen = set()
        pq = [(0, 0, 0)]

        while pq:
            effort, x, y = heapq.heappop(pq)
            if x == n - 1 and y == m - 1:
                return effort
            if (x, y) not in seen:
                seen.add((x, y))
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen:
                        new_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))
                        heapq.heappush(pq, (new_effort, nx, ny))

