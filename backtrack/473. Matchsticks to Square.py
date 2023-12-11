class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        lengths = [0, 0, 0, 0]

        total = sum(matchsticks)
        length = total // 4

        matchsticks.sort(reverse=True)

        if total % 4 != 0 or matchsticks[0] > length:
            return False
        

        def backtrack(index):
            if index == n:
                return True
            
            for i in range(4):
                # 
                if lengths[i] + matchsticks[index] <= length:
                    lengths[i] += matchsticks[index]

                    if backtrack(index+1):
                        return True
                    
                    lengths[i] -= matchsticks[index]
            return False
        
        return backtrack(0)
            
        