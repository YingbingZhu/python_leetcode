class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        middle = k // 2
        if n < middle:
            return (n * n + n) // 2

        # include all number < middle
        res = (middle * middle + middle) // 2

        n -= middle

        while n > 0:
            res += k
            k += 1
            n -= 1

        return res
