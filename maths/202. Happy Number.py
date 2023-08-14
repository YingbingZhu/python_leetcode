class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            cur = 0
            while n:
                cur += (n % 10) **2
                n //= 10
            if cur in seen:
                return False
            seen.add(cur)
            n = cur
        return True
             