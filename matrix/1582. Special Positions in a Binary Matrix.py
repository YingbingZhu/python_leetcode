class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        rows = [sum(mat[i]) for i in range(len(mat))]
        cols = [sum(col) for col in zip(*mat)]
        

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    ans += 1
        return ans