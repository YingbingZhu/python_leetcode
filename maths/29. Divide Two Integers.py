class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = ((dividend < 0) != (divisor < 0))
        left = abs(dividend)
        div = abs(divisor)
        ans = 0
        q = 1
        while left >= div:
            left -= div
            ans += q
            # double to decrease time
            q += q
            div += div
            if left < div:
                q = 1
                div = abs(divisor)
        if neg:
            return max(-2 ** 31, -ans)
        else:
            return min(2 ** 31 - 1, ans)
