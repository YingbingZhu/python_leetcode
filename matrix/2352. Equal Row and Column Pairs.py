class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            for col in zip(*grid):
                if row == list(col):
                    res += 1
        return res