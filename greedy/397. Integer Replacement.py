class Solution:
    def integerReplacement(self, n: int) -> int:


        def helper(i):
            if i == 1:
                return 0
            if i == 2:
                return 1
            if i % 2 == 0:
                return 1 + helper(i//2)
            else:
                return 1 + min(helper(i-1), helper(i+1))
        
        return helper(n)