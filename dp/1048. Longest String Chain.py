class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        dp = defaultdict(int)
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                pre = word[:i] + word[i+1:]
                dp[word] = max(dp[word], dp[pre] + 1)
        return max(dp.values())