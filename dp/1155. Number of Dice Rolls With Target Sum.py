# You have n dice and each die has k faces numbered from 1 to k.
#
# Given three integers n, k, and target,
# return the number of possible ways (out of the kn total ways)
# to roll the dice so the sum of the face-up numbers equals target.
# Since the answer may be too large, return it modulo 109 + 7.

class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        # fix one dice at a time
        # dp(d, f, t) = dp(d-1, f, t-1)+...+dp(d-1, f, t-f)
        return self.dp(n, k, target, {}) % (10 ** 9 + 7)

    def dp(self, n, k, target, memo):
        # base case
        if n == 0:
            if target == 0:
                return 1
            else:
                return 0
        if (n, target) in memo:
            return memo[(n, target)]
        res = 0
        for i in range(1, k + 1):
            res += self.dp(n - 1, k, target - i, memo)
        memo[(n, target)] = res
        return memo[(n, target)]