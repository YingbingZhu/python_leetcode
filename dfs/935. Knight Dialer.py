class Solution:
    def knightDialer(self, n: int) -> int:
        next_move = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dirs = [[2,1], [1,2], [-2,1], [-1,2], [2,-1], [1,-2], [-2,-1], [-1,-2]]


        @cache
        def dfs(index, i, j):
            if index == n - 1:
                return 1
            ans = 0
            for ii, jj in [[i + dir[0], j + dir[1]] for dir in dirs]:
                if (-1<ii<3 and -1<jj<3) or (ii==3 and jj==1):
                    ans += dfs(index+1, ii, jj) 
            return ans % (10**9 + 7)


        ans = dfs(0, 3, 1)
        for row in range(3):
            for col in range(3):
                ans += dfs(0, row, col)

        return ans % (10**9 + 7)
                
        

        

        