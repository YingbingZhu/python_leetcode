class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        mod = 10**9 + 7

        def dfs(target, dp):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if dp[target] != -1:
                return dp[target]
            curr = dfs(target - one, dp) + dfs(target - zero, dp)
            dp[target] = curr % mod
            return dp[target]

        ans = 0
        dp = [-1] * (high+1)
        for i in range(low, high+1):
            dfs(i, dp)
            ans = (ans % mod + dp[i]) % mod
        return ans

