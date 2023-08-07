class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        n = len(grid)
        q = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        # find the minimum mahatten distance of each cell to theives
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= rr < n and 0 <= cc < n and grid[rr][cc] == 0:
                        q.append((rr, cc))
                        grid[rr][cc] = grid[r][c] + 1

        seen = set([0, 0])
        # dijkstra
        heap = [[-grid[0][0], 0, 0]]
        res = inf
        while heap:
            for _ in range(len(heap)):
                cur, r, c = heapq.heappop(heap)
                res = min(res, -cur)
                if r == n - 1 and c == n - 1:
                    return res - 1
                for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= rr < n and 0 <= cc < n and (rr, cc) not in seen:
                        heapq.heappush(heap, [-grid[rr][cc], rr, cc])
                        seen.add((rr, cc))

        return -1



