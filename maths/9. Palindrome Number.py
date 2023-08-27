class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = 0
        x1 = x
        cnt = 1
        while x > 0:
            b = b * 10 + x % 10
            x //= 10
        return b == x1