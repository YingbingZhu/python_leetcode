class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        # will have duplicate if n > 10
        n = min(10, n)
        

        # base case, 10 choices, i = 1
        cnt = 10
        
        # 10 [0, ...., 9]
        # 9 * 9  [1, .... 9] * [0, .... 9] ( except one)
        # 9 * 9 * 8
        for i in range(2, n + 1):
            choices = 9
            for j in range(i - 1):
                choices *= 9 - j
            cnt += choices
        
        return cnt