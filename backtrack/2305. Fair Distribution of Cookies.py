class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        avg = sum(cookies) // k
        cur = [0] * k
        self.ans = float('inf')

        def dfs(cur, i):
            if i == len(cookies):
                self.ans = min(self.ans, max(cur))
                return
            # skip if any kid has more of current unfairness
            if max(cur) >= self.ans:
                return
            for j in range(k):
                cur[j] += cookies[i]
                dfs(cur, i+1)
                cur[j] -= cookies[i]
        
        dfs(cur, 0)
        return self.ans
        